
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kicks on 1 and 3, snares on 2 and 4, hihats on every eighth
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
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no same note twice
# Fm7 = F, Ab, C, Eb
# Bass line in Fm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # Eb
    # Fill
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # Eb
    # Finish
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bars 2-4: chords on 2 and 4

# Bar 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
]
# Bar 3
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F
]
# Bar 4
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: motif, short, sing, start, leave it hanging, come back and finish
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F, Ab, Bb, B (from Fm scale), then repeat starting on Ab

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=75, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=73, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.5),  # B
]
# Bar 3
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=75, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=73, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.5),  # F
]
# Bar 4
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=75, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=73, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=110, pitch=77, start=4.25, end=4.5),  # F
]
# Fill
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=75, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=73, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=110, pitch=77, start=5.25, end=5.5),  # F
]
# Finish
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=75, start=5.5, end=5.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=73, start=5.75, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
