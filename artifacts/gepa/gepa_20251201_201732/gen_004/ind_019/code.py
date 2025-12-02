
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Fm (F2, C2, Bb2, Ab2, G2, F2, Eb2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=34, start=1.875, end=2.25), # C2
    pretty_midi.Note(velocity=100, pitch=33, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=100, pitch=31, start=2.625, end=3.0),  # Ab2
]

# Diane: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),  # Ab (A3)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # C (D4)
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),  # Db (C#4)
]

# Dante: Sax begins with a motif: F, Ab, G, Eb (Fm6)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Ab (G4)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # Eb (E4)
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in Fm (F2, C2, Bb2, Ab2, G2, F2, Eb2, Db2)
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=34, start=3.375, end=3.75), # C2
    pretty_midi.Note(velocity=100, pitch=33, start=3.75, end=4.125), # Bb2
    pretty_midi.Note(velocity=100, pitch=31, start=4.125, end=4.5),  # Ab2
])

# Diane: Bbmaj7 (Bb, D, F, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # Bb (A3)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # D (C#4)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # G (D4)
])

# Dante: Continue motif with variation: Bb, F, Eb, F (Fm6)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # Eb (E4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F (F4)
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in Fm (F2, C2, Bb2, Ab2, G2, F2, Eb2, Db2)
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=34, start=4.875, end=5.25), # C2
    pretty_midi.Note(velocity=100, pitch=33, start=5.25, end=5.625), # Bb2
    pretty_midi.Note(velocity=100, pitch=31, start=5.625, end=6.0),  # Ab2
])

# Diane: Fm7 (F, Ab, C, Db)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=6.0),  # Ab (A3)
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),  # C (D4)
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),  # Db (C#4)
])

# Dante: Sax ends motif: F, Ab, G, Eb (Fm6)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Ab (G4)
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # Eb (E4)
])

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Add drum fills for bar 2-4
# Bar 2: Fill on 3 (kick, snare, hihat)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.125),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),    # Hihat
])

# Bar 3: Fill on 3 (kick, snare, hihat)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.375, end=4.625),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),    # Hihat
])

# Bar 4: Fills on 2 and 3 (snare, kick, hihat)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),    # Hihat
])

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
