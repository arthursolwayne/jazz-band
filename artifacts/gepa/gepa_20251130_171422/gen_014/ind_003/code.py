
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 4/4 time and 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
time_signature = pretty_midi.TimeSignature(4, 4, 0)
pm.time_signature_changes.append(time_signature)

# Define the key: F minor
# Fm = F, Ab, Bb
# Scale degrees: 1=F, 2=G, 3=Ab, 4=Bb, 5=C, 6=Db, 7=Eb

# Define the note values in MIDI pitches
note_map = {
    'F': 65, 'G': 67, 'Ab': 68, 'Bb': 70, 'C': 72, 'Db': 73, 'Eb': 74
}

# Define the instruments
# Drum Kit
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum_instrument = pretty_midi.Instrument(program=drum_program, is_drum=True)
pm.instruments.append(drum_instrument)

# Bass
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# Piano
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# Saxophone (Tenor)
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# TIME = 0.0

# BEAT = 0.375s, 4/4 time
# 1 bar = 1.5s

# Bar 1: Little Ray alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kicks on 1 and 3
for beat in [0, 2]:
    kick_time = beat * 0.375
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drum_instrument.notes.append(kick_note)

# Snares on 2 and 4
for beat in [1, 3]:
    snare_time = beat * 0.375
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drum_instrument.notes.append(snare_note)

# Hi-hats on every eighth note (8 notes per bar)
for eighth in range(8):
    hihat_time = eighth * 0.1875
    hihat_note = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.05)
    drum_instrument.notes.append(hihat_note)

# Bar 2: Everyone in
# Start time = 1.5s

# Bass: Walking line, chromatic approach
# Fm = F, Ab, Bb
# Walking line: F -> G -> Ab -> Bb -> C -> Db -> Eb -> F

bass_notes = [
    note_map['F'], note_map['G'], note_map['Ab'], note_map['Bb'],
    note_map['C'], note_map['Db'], note_map['Eb'], note_map['F']
]

# Start at bar 2 (1.5s)
bass_start = 1.5
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=bass_start + i * 0.375,
        end=bass_start + i * 0.375 + 0.25
    )
    bass_instrument.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# G7 = G, Bb, D, F
# Ab7 = Ab, C, Eb, G
# Bb7 = Bb, D, F, Ab

chords = [
    # Bar 2 (beat 1): F7
    [note_map['F'], note_map['A'], note_map['C'], note_map['Eb']],
    # Bar 2 (beat 2): G7
    [note_map['G'], note_map['Bb'], note_map['D'], note_map['F']],
    # Bar 2 (beat 3): Ab7
    [note_map['Ab'], note_map['C'], note_map['Eb'], note_map['G']],
    # Bar 2 (beat 4): Bb7
    [note_map['Bb'], note_map['D'], note_map['F'], note_map['Ab']]
]

# Comp on 2 and 4 (beats 2 and 4)
comp_times = [1.5 + 0.75, 1.5 + 1.5]
for beat, time in enumerate(comp_times):
    for pitch in chords[beat]:
        note = pretty_midi.Note(
            velocity=95,
            pitch=pitch,
            start=time,
            end=time + 0.2
        )
        piano_instrument.notes.append(note)

# Saxophone: Motif with space
# Motif = F -> Ab -> Bb -> [space] -> F
# Start at bar 2 (1.5s), 0.5s into the bar

sax_notes = [
    note_map['F'], note_map['Ab'], note_map['Bb']
]

sax_times = [1.5 + 0.5, 1.5 + 0.875, 1.5 + 1.25]
for i, (pitch, time) in enumerate(zip(sax_notes, sax_times)):
    note = pretty_midi.Note(
        velocity=110,
        pitch=pitch,
        start=time,
        end=time + 0.25
    )
    sax_instrument.notes.append(note)

# Bar 3: Everyone in again (same as bar 2 but different motif)
# Bass: Walk again, same line
# Piano: 7th chords again
# Sax: Second motif, F -> G -> Eb -> [space]

# Bass: same as before, start at 3.0s
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=3.0 + i * 0.375,
        end=3.0 + i * 0.375 + 0.25
    )
    bass_instrument.notes.append(note)

# Piano: same chords, comp on 2 and 4
comp_times = [3.0 + 0.75, 3.0 + 1.5]
for beat, time in enumerate(comp_times):
    for pitch in chords[beat]:
        note = pretty_midi.Note(
            velocity=95,
            pitch=pitch,
            start=time,
            end=time + 0.2
        )
        piano_instrument.notes.append(note)

# Sax: new motif
sax_notes = [
    note_map['F'], note_map['G'], note_map['Eb']
]

sax_times = [3.0 + 0.5, 3.0 + 0.875, 3.0 + 1.25]
for i, (pitch, time) in enumerate(zip(sax_notes, sax_times)):
    note = pretty_midi.Note(
        velocity=110,
        pitch=pitch,
        start=time,
        end=time + 0.25
    )
    sax_instrument.notes.append(note)

# Bar 4: Everyone in again (same as bar 2 and 3 but final motif)
# Bass: walk again
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(
        velocity=90,
        pitch=pitch,
        start=4.5 + i * 0.375,
        end=4.5 + i * 0.375 + 0.25
    )
    bass_instrument.notes.append(note)

# Piano: comp again
comp_times = [4.5 + 0.75, 4.5 + 1.5]
for beat, time in enumerate(comp_times):
    for pitch in chords[beat]:
        note = pretty_midi.Note(
            velocity=95,
            pitch=pitch,
            start=time,
            end=time + 0.2
        )
        piano_instrument.notes.append(note)

# Sax: final, unresolved motif
# F -> Ab -> [space] -> Ab (leaves it hanging)
sax_notes = [note_map['F'], note_map['Ab']]
sax_times = [4.5 + 0.5, 4.5 + 0.875]
for i, (pitch, time) in enumerate(zip(sax_notes, sax_times)):
    note = pretty_midi.Note(
        velocity=110,
        pitch=pitch,
        start=time,
        end=time + 0.25
    )
    sax_instrument.notes.append(note)

# Save to MIDI file
pm.write("dante_intro.mid")
print("MIDI file generated as 'dante_intro.mid'")
