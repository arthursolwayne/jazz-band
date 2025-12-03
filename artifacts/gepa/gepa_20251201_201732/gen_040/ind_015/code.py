
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # A2 (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),  # A2
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C#4 (low)
    # Bar 3: D7 (D-F#-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # C4 (low)
    # Bar 4: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C4 (low)
    # Bar 2: comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75),  # C4 (low)
    # Bar 3: comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=3.875),  # C4 (low)
    # Bar 4: comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625),  # C4 (low)
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # E4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
# Snare on 2 and 4
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
# Hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
