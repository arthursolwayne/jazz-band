
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: D minor (key number 29)
midi.key_signature_changes = [pretty_midi.KeySignature(29, 0)]

# Tempo: 160 BPM
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Bar = 1.5 seconds, beat = 0.375 sec
bar_length = 1.5
beat_length = 0.375
bar_count = 4

# ------------------------------
# Drums: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Fill the bar with energy, but not overwhelming
# ------------------------------

for bar in range(bar_count):
    for i in range(8):  # 8 eighth notes per bar
        time = bar * bar_length + i * beat_length / 2
        if i % 2 == 0:
            # Hihat on every eighth
            hihat = pretty_midi.Note(
                velocity=80,
                pitch=pretty_midi.note_number_to_name(42)[1],  # C4
                start=time,
                end=time + beat_length / 2
            )
            drums.notes.append(hihat)
        if i == 0 or i == 4:
            # Kick on 1 and 3
            kick = pretty_midi.Note(
                velocity=100,
                pitch=pretty_midi.note_number_to_name(36)[1],  # C2
                start=time,
                end=time + beat_length / 2
            )
            drums.notes.append(kick)
        if i == 2 or i == 6:
            # Snare on 2 and 4
            snare = pretty_midi.Note(
                velocity=90,
                pitch=pretty_midi.note_number_to_name(62)[1],  # G4
                start=time,
                end=time + beat_length / 2
            )
            drums.notes.append(snare)

# ------------------------------
# Bass: Marcus
# Walking line with chromatic approaches, no repeating notes
# Dm: D, F, A, C
# Chromatic approaches: C#, D#, F#, G#, A#, B, C
# ------------------------------

# Bass line in Dm: D, F, A, C, G (chromatic approach to A), C#, D, F
bass_notes = [
    (0, 2.0),        # D (2nd beat)
    (5, 2.5),        # F (3rd beat)
    (9, 3.0),        # A (4th beat)
    (11, 3.5),       # C (1st beat)
    (7, 4.0),        # G (approach to A)
    (1, 4.5),        # C#
    (3, 5.0),        # D
    (5, 5.5),        # F
]

for note, time in bass_notes:
    start = time
    end = start + beat_length / 2
    bass_note = pretty_midi.Note(
        velocity=90,
        pitch=note + 24,  # Middle C is 60, so D is 62
        start=start,
        end=end
    )
    bass.notes.append(bass_note)

# ------------------------------
# Piano: Diane
# 7th chords, comp on 2 and 4 (beat 2 and beat 4)
# Dm7: D, F, A, C
# 7th chords in root position: D, F, A, C
# Play on beat 2 and 4
# ------------------------------

# Dm7: D, F, A, C
# Play on beats 2 and 4 of each bar
for bar in range(bar_count):
    for beat in [1, 3]:  # beat 2 and 4 (0-based)
        time = bar * bar_length + beat * beat_length
        # Dm7: D, F, A, C
        for note in [2, 5, 9, 11]:
            piano_note = pretty_midi.Note(
                velocity=80,
                pitch=note + 48,  # Middle C is 60, so D is 62
                start=time,
                end=time + beat_length / 2
            )
            piano.notes.append(piano_note)

# ------------------------------
# Tenor Sax: Dante
# One short motif, make it sing.
# Dm: D, F, A, C
# Motif: D -> F -> A -> rest (hang it)
# Then come back and finish it: D -> F -> A -> C (resolve)
# ------------------------------

# Bar 1: Silence (Little Ray alone)
# Bar 2-4: You play

# Bar 2: D -> F -> A -> rest
# Bar 3: D -> F -> A -> C

# Bar 2
note_d = pretty_midi.Note(
    velocity=100,
    pitch=62,  # D4
    start=1.5,  # start of bar 2
    end=1.5 + 0.375 / 2
)
note_f = pretty_midi.Note(
    velocity=100,
    pitch=65,  # F4
    start=1.5 + 0.375,
    end=1.5 + 0.375 + 0.375 / 2
)
note_a = pretty_midi.Note(
    velocity=100,
    pitch=67,  # A4
    start=1.5 + 0.75,
    end=1.5 + 0.75 + 0.375 / 2
)
sax_notes = [note_d, note_f, note_a]

# Bar 3
note_d2 = pretty_midi.Note(
    velocity=100,
    pitch=62,
    start=3.0,
    end=3.0 + 0.375 / 2
)
note_f2 = pretty_midi.Note(
    velocity=100,
    pitch=65,
    start=3.0 + 0.375,
    end=3.0 + 0.375 + 0.375 / 2
)
note_a2 = pretty_midi.Note(
    velocity=100,
    pitch=67,
    start=3.0 + 0.75,
    end=3.0 + 0.75 + 0.375 / 2
)
note_c = pretty_midi.Note(
    velocity=100,
    pitch=69,  # C5
    start=3.0 + 1.125,
    end=3.0 + 1.125 + 0.375 / 2
)
sax_notes.extend([note_d2, note_f2, note_a2, note_c])

# Add to saxophone instrument
sax = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Tenor Saxophone'))
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments = [bass, piano, drums, sax]

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
