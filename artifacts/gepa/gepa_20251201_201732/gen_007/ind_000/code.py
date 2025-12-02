
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)    # Snare on 4 (but bar ends at 1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (F2 - Bb2) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # E2
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),   # G2
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),   # F2
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75),  # Eb2
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # E2
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),   # G2
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),   # F2
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # E2
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),   # G2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # Eb4
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=3.0),  # Ab4
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # Bb4
])
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):  # Bars 2, 3, 4
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=90, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=90, pitch=38, start=start + 1.5, end=start + 1.875)

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),   # F4 (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
