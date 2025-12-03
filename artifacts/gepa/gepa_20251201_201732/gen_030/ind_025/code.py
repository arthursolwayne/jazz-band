
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

# Bass (Marcus) - Walking line in Fm (F, Ab, D, C, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # Bb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # A2 (chromatic approach)

    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # F2 (root)
    pretty_midi.Note(velocity=90, pitch=37, start=4.125, end=4.5),  # Eb2 (chromatic approach)

    pretty_midi.Note(velocity=90, pitch=37, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),  # Gb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, resolve on the last beat of each bar
# Bar 2: Fm7 (F, Ab, C, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # Db4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Ab4

    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # Db4
]
piano.notes.extend(piano_notes)

# Drums (Little Ray) - Full kit, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)

# Sax (Dante) - One short motif, start it, leave it hanging. Come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Ab4

    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F4
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # Ab4

    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # Ab4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
