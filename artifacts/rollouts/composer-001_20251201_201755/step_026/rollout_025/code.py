
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (D2) - G2 (G2) - F2 (F2) - E2 (E2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # F2
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # E2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (beat 1), F4 (beat 2), A4 (beat 3), D4 (beat 4) but only play first three notes
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # A4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (G2) - A2 (A2) - B2 (B2) - D3 (D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # B2
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # Bb4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif (D4 on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (D2) - F2 (F2) - G2 (G2) - D2 (D2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),   # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif (D4), but don't resolve it, leave it open
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
