
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625),  # D2
    pretty_midi.Note(velocity=90, pitch=39, start=1.625, end=1.75),  # chromatic
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),  # D2

    # Bar 3: G2 (fifth), Bb2 (chromatic), C2 (root), D2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.125),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.125, end=2.25),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=2.375, end=2.5),  # F2

    # Bar 4: Bb2 (chromatic), D2 (root), F2 (fifth), Ab2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=2.75),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=2.75, end=2.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=2.875, end=3.0),  # Gb2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicings, resolving on last bar
piano_notes = [
    # Bar 2: Dm7 no 5, Eb7 no 5
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625),  # C5

    # Bar 3: G7 no 5, Ab7 no 5
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.125),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.125),  # D5

    # Bar 4: C7 no 5, Dm7 no 5 (resolve)
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.625),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.625),  # E5
    pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=2.625),  # F5
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=2.625),  # A5
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short, haunting motif
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # Ab5

    # Bar 3: Repeat with slight variation
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.25),  # F5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # Ab5

    # Bar 4: Return and resolve, leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # F5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue with kick, snare, and hihat
drum_notes_continued = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),  # kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.125),  # kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),  # kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),  # snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
]

for note in drum_notes_continued:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
