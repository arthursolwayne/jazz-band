
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(120.0, 0.0)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line in C, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 60), (1.75, 61), (2.0, 62), (2.25, 63),
    # Bar 3
    (2.5, 60), (2.75, 61), (3.0, 62), (3.25, 63),
    # Bar 4
    (3.5, 60), (3.75, 61), (4.0, 62), (4.25, 63)
]
for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Diane on piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 60), (1.75, 64), (1.75, 67), (1.75, 71),  # C7
    (2.25, 60), (2.25, 64), (2.25, 67), (2.25, 71),  # C7
    # Bar 3 (3.0 - 4.5s)
    (3.25, 60), (3.25, 64), (3.25, 67), (3.25, 71),  # C7
    (3.75, 60), (3.75, 64), (3.75, 67), (3.75, 71),  # C7
    # Bar 4 (4.5 - 6.0s)
    (4.75, 60), (4.75, 64), (4.75, 67), (4.75, 71),  # C7
    (5.25, 60), (5.25, 64), (5.25, 67), (5.25, 71),  # C7
]
for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    piano.notes.append(note)

# Dante on sax: Motif in C
# Motif: C (60), E (64), B (67), D (62), rest
# Start bar 2 (1.5s), repeat at 2.5s, end at 3.0s
sax_notes = [
    (1.5, 60), (1.5, 64), (1.5, 67), (1.5, 62),  # C, E, B, D
    (2.5, 60), (2.5, 64), (2.5, 67), (2.5, 62),  # Repeat
    (3.0, 60), (3.0, 64), (3.0, 67), (3.0, 62)   # End on D
]
for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + 0.25)
    sax.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write('dante_intro.mid')
