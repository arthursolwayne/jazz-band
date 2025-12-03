
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
    pretty_midi.Note(velocity=110, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=110, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start and leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Fm7
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # Fm7
]
sax.notes.extend(sax_notes)

# Bass: walking line in Fm (roots and fifths with chromatic approaches)
# Bar 2: F -> Ab -> Bb -> C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G (chromatic approach to Bb)
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: open voicing, Fm7 -> Ab7 -> Bb7 -> C7
# Comp on 2 and 4
piano_notes = [
    # Fm7 (bar 2, beat 2)
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Ab
    # Ab7 (bar 3, beat 2)
    pretty_midi.Note(velocity=100, pitch=56, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    # Bb7 (bar 4, beat 2)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D
    # C7 (bar 4, beat 4)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # Fm7
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: walking line
# Bar 3: C -> Eb -> F -> G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),  # F (chromatic approach to F)
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: open voicing, Ab7 -> Bb7 -> C7
# Comp on 2 and 4
piano_notes = [
    # Ab7 (bar 3, beat 2)
    pretty_midi.Note(velocity=100, pitch=56, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    # Bb7 (bar 4, beat 2)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D
    # C7 (bar 4, beat 4)
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: continuation of motif with resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Fm7
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Fm7
]
sax.notes.extend(sax_notes)

# Bass: walking line
# Bar 4: G -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=5.25, end=5.625),  # B (chromatic approach to Bb)
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: C7 (bar 4, beat 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 3-4
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=110, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
