
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
    # Hi-hat on every eighth
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

# Bass: Walking line with chromatic approaches
# Bar 2: D2 (root), Bb2 (chromatic approach), G2 (fifth), C2 (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.25),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=3.0),  # C2
    # Bar 3: G2 (root), E2 (chromatic), B2 (fifth), D2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # E2
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # B2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # D2
    # Bar 4: B2 (root), G2 (chromatic), D2 (fifth), F2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),  # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C#5
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F4
    # Bar 4: Bm7 (B-D-F#-A)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # F#5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # A5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing
# Melody: D4 (start), F#4, A4, D4 (resolve)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for Bars 2-4
# Same pattern as Bar 1
for i in range(3):
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5 + i * 1.5, note.end + 1.5 + i * 1.5)
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
