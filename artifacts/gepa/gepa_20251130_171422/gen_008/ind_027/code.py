
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor (F, Gb, Ab, Bb, C, Db, Eb)
# Scale degrees: 1 (F), 2 (Gb), 3 (Ab), 4 (Bb), 5 (C), 6 (Db), 7 (Eb)

# Time signatures: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the tempo
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
# 1. Tenor Sax (MIDI program 64)
sax_program = pretty_midi.programs.Program(64)
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# 2. Bass (MIDI program 33)
bass_program = pretty_midi.programs.Program(33)
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# 3. Piano (MIDI program 0)
piano_program = pretty_midi.programs.Program(0)
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# 4. Drums (MIDI program 128)
drum_program = pretty_midi.programs.Program(128)
drum_instrument = pretty_midi.Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# Define note values in seconds
beat = 0.375  # 160 BPM = 60 / 160 = 0.375 seconds per beat
note_lengths = {
    '16n': beat / 4,
    '8n': beat / 2,
    '4n': beat,
    '2n': beat * 2,
    '1n': beat * 4
}

# Drums: Bar 1 - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 0: Kick, 1: Snare, 10: Hihat
# Bar 1 (0-1.5s)
drum_notes = [
    (0, 0, 0),  # Kick on 1
    (1, 0.375, 0),  # Snare on 2
    (10, 0, 0),  # Hihat on 1
    (10, 0.1875, 0),  # Hihat on 1 &
    (10, 0.375, 0),  # Hihat on 2
    (10, 0.5625, 0),  # Hihat on 2 &
    (10, 0.75, 0),  # Hihat on 3
    (10, 0.9375, 0),  # Hihat on 3 &
    (10, 1.125, 0),  # Hihat on 4
    (10, 1.3125, 0),  # Hihat on 4 &
    (0, 1.125, 0),  # Kick on 3
    (1, 1.5, 0)  # Snare on 4
]
for note, time, velocity in drum_notes:
    drum_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + note_lengths['16n']))

# Bar 2: Everyone comes in
# Tenor Sax: Start of the melody
# Fm - Start with F (F), move to C (5th), then to Bb (4th), Ab (3rd)
# Motif: F -> C -> Bb -> Ab (each on a quarter note)
# Play F, rest on C, play Bb, rest on Ab

sax_notes = [
    (60, 0, 100),  # F (60) at time 1.5s (start of Bar 2)
    (65, 1.5, 0),  # Rest on C (65)
    (62, 2.25, 100),  # Bb (62)
    (61, 3.0, 0),  # Rest on Ab (61)
    (61, 3.0, 100),  # Play Ab (61) on beat 4
]
for pitch, start, velocity in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_lengths['1n']))

# Bass: Walking line in Fm
# F -> Gb -> Ab -> Bb -> C -> Db -> Eb -> F
# Start on F (60) on beat 1, walk down the scale
bass_notes = [
    (60, 1.5, 70),  # F (60)
    (61, 1.875, 70),  # Gb (61)
    (62, 2.25, 70),  # Ab (62)
    (63, 2.625, 70),  # Bb (63)
    (64, 3.0, 70)  # C (64)
]
for pitch, start, velocity in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_lengths['8n']))

# Piano: Comp on 2 and 4 with 7th chords
# Bar 2: F7 (F, Ab, C, Eb) on beat 2
# Bar 2: Bb7 (Bb, Db, F, Ab) on beat 4

# F7 on beat 2
piano_notes = [
    (60, 1.875, 80),  # F
    (63, 1.875, 80),  # Ab
    (64, 1.875, 80),  # C
    (67, 1.875, 80),  # Eb
]

# Bb7 on beat 4
piano_notes += [
    (62, 3.0, 80),  # Bb
    (65, 3.0, 80),  # Db
    (60, 3.0, 80),  # F
    (63, 3.0, 80)  # Ab
]

for pitch, start, velocity in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_lengths['1n']))

# Bar 3 and 4: Tenor Sax finishes the motif
# Continue the motif from Bar 2: F -> C -> Bb -> Ab -> F (octave up)
# Play the Ab (61), then F (60), then Gb (61), then Ab (62) again
sax_notes = [
    (61, 3.0, 100),  # Ab
    (60, 3.375, 100),  # F
    (61, 3.75, 100),  # Gb
    (62, 4.125, 100)  # Ab
]
for pitch, start, velocity in sax_notes:
    sax_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_lengths['8n']))

# Bass: Continue the walking line
bass_notes = [
    (65, 3.375, 70),  # Db
    (66, 3.75, 70),  # Eb
    (60, 4.125, 70)  # F
]
for pitch, start, velocity in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_lengths['8n']))

# Piano: Comp on 2 and 4 again
# Bar 3: C7 (C, Eb, G, Bb) on beat 2
# Bar 4: Ab7 (Ab, Bb, Db, F) on beat 4
piano_notes = [
    # Bar 3: C7 on beat 2
    (64, 3.375, 80),  # C
    (67, 3.375, 80),  # Eb
    (71, 3.375, 80),  # G
    (62, 3.375, 80),  # Bb

    # Bar 4: Ab7 on beat 4
    (62, 4.5, 80),  # Ab
    (63, 4.5, 80),  # Bb
    (65, 4.5, 80),  # Db
    (60, 4.5, 80)  # F
]
for pitch, start, velocity in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_lengths['1n']))

# Drums: Bar 3 and 4
# Same pattern: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 1.5
for bar in range(2, 4):
    # Kick on 1 and 3
    drum_notes = [
        (0, bar_start + 0, 0),
        (0, bar_start + 1.125, 0),
        (1, bar_start + 0.375, 0),  # Snare on 2
        (1, bar_start + 1.5, 0),  # Snare on 4
    ]
    # Hihat on every eighth
    for i in range(8):
        time = bar_start + 0.1875 * i
        drum_notes.append((10, time, 0))
    for note, time, velocity in drum_notes:
        drum_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + note_lengths['16n']))

# Write the MIDI file
pm.write("Fm_intro.mid")
print("MIDI file generated as 'Fm_intro.mid'")
