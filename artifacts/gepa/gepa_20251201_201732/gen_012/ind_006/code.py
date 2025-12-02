
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.key_signature_changes = [pretty_midi.KeySignature(-1, 0)]  # F minor

# Tempo
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
tenor_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
tenor = pretty_midi.Instrument(program=tenor_program)

pm.instruments = [bass, piano, drums, tenor]

# Define timing
BPM = 160
beats_per_bar = 4
notes_per_beat = 4
note_length = 1 / (BPM / 60)  # seconds per beat
bar_length = note_length * beats_per_bar

# Utility to convert bar index to time
def bar_to_time(bar):
    return bar * bar_length

# --- DRUMS: Kick, Snare, Hihat ---
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums():
    bar = 0
    time_start = bar_to_time(bar)

    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(
            velocity=100, pitch=36, start=time_start + beat * note_length / 4 * 2,
            end=time_start + beat * note_length / 4 * 2 + note_length / 4 * 2
        )
        drums.notes.append(note)

    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(
            velocity=100, pitch=38, start=time_start + beat * note_length / 4 * 2,
            end=time_start + beat * note_length / 4 * 2 + note_length / 4 * 2
        )
        drums.notes.append(note)

    # Hihat on every eighth note (8 notes per bar)
    for i in range(8):
        note = pretty_midi.Note(
            velocity=80, pitch=42, start=time_start + i * note_length / 8,
            end=time_start + i * note_length / 8 + note_length / 8
        )
        drums.notes.append(note)

# --- BASS: Walking line in F minor (roots and fifths with chromatic approach) ---
def add_bass():
    # Fm: F, Gb, Ab, Bb, C, Db, Eb
    # Bar 1: F -> Gb (chromatic approach)
    # Bar 2: Ab -> Bb
    # Bar 3: C -> Db
    # Bar 4: Eb -> F

    bar = 0
    time_start = bar_to_time(bar)
    note_length = note_length / 2  # half note

    # Bar 1: F -> Gb
    for note, next_note in [(65, 66)]:
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time_start, end=time_start + note_length)
        bass.notes.append(note_obj)
        note_obj = pretty_midi.Note(velocity=80, pitch=next_note, start=time_start + note_length, end=time_start + note_length * 2)
        bass.notes.append(note_obj)

    # Bar 2: Ab -> Bb
    for note, next_note in [(69, 71)]:
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time_start + bar_length, end=time_start + bar_length + note_length)
        bass.notes.append(note_obj)
        note_obj = pretty_midi.Note(velocity=80, pitch=next_note, start=time_start + bar_length + note_length, end=time_start + bar_length + note_length * 2)
        bass.notes.append(note_obj)

    # Bar 3: C -> Db
    for note, next_note in [(60, 61)]:
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time_start + bar_length * 2, end=time_start + bar_length * 2 + note_length)
        bass.notes.append(note_obj)
        note_obj = pretty_midi.Note(velocity=80, pitch=next_note, start=time_start + bar_length * 2 + note_length, end=time_start + bar_length * 2 + note_length * 2)
        bass.notes.append(note_obj)

    # Bar 4: Eb -> F
    for note, next_note in [(64, 65)]:
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time_start + bar_length * 3, end=time_start + bar_length * 3 + note_length)
        bass.notes.append(note_obj)
        note_obj = pretty_midi.Note(velocity=80, pitch=next_note, start=time_start + bar_length * 3 + note_length, end=time_start + bar_length * 3 + note_length * 2)
        bass.notes.append(note_obj)

# --- PIANO: Open voicings, one chord per bar, comp on 2 and 4 ---
def add_piano():
    # Bar 1: Fm7 (F, Ab, C, Eb)
    # Bar 2: Ab7 (Ab, C, Eb, Gb)
    # Bar 3: Bb7 (Bb, D, F, Ab)
    # Bar 4: Cm7 (C, Eb, G, Bb)
    chords = [
        [65, 69, 60, 64],  # Fm7
        [69, 60, 64, 66],  # Ab7
        [71, 62, 65, 69],  # Bb7
        [60, 64, 67, 71],  # Cm7
    ]

    for bar_idx, chord in enumerate(chords):
        time_start = bar_to_time(bar_idx)

        # Open voicings, spaced out
        for note in chord:
            note_obj = pretty_midi.Note(
                velocity=80, pitch=note, start=time_start, end=time_start + (bar_length / 2)  # comp on 2 and 4
            )
            piano.notes.append(note_obj)

# --- TENOR SAX: One short motif, start it, leave it hanging, come back and finish it ---
def add_tenor():
    # Fm scale: F, Gb, Ab, Bb, C, Db, Eb
    # Motif: F -> Ab -> Bb -> (rest) -> C
    # Start on bar 1, leave it hanging on the third note, resolve on the fourth

    notes = [65, 69, 71, 60]  # F, Ab, Bb, C
    durations = [0.375, 0.375, 0.375, 0.375]
    bar = 0
    time_start = bar_to_time(bar)

    # Play the first three notes
    for i in range(3):
        note_obj = pretty_midi.Note(velocity=100, pitch=notes[i], start=time_start + sum(durations[:i]), end=time_start + sum(durations[:i+1]))
        tenor.notes.append(note_obj)

    # Let it hang — rest for the duration of the fourth note
    # Then resolve on the fourth note
    note_obj = pretty_midi.Note(velocity=100, pitch=notes[3], start=time_start + sum(durations[:3]), end=time_start + sum(durations[:4]))
    tenor.notes.append(note_obj)

# --- Execute the parts ---
add_drums()
add_bass()
add_piano()
add_tenor()

# Save the MIDI file
pm.write('dante_intro.mid')

print("MIDI file 'dante_intro.mid' has been created.")
print("Listen, Wayne. You're gonna lean forward.")
