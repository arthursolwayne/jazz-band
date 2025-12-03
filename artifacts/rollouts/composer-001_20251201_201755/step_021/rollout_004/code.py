
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
bar_length = 1.5  # seconds per bar at 160 BPM

# Drums - Bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus (walking line in Fm, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=2.0),  # Ab2
    pretty_midi.Note(velocity=80, pitch=39, start=2.0, end=2.25),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.5),  # G#2
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.75),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0),  # Bb2 (fifth of Fm)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=3.25, end=3.5),  # Ab2
    pretty_midi.Note(velocity=80, pitch=40, start=3.5, end=3.75),  # G#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=39, start=3.75, end=4.0),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.25),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.5),  # Bb2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.75),  # F2
    pretty_midi.Note(velocity=80, pitch=41, start=4.75, end=5.0),  # Ab2
    pretty_midi.Note(velocity=80, pitch=40, start=5.0, end=5.25),  # G#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.5),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=5.75),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=6.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano - Diane (open voicings, different chord each bar, resolve on the last)
# Bar 2 (1.5 - 3.0s): Fm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # F4 (root)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # Ab4 (minor third)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # Bb4 (fifth)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # D4 (minor seventh)

    # Bar 3 (3.0 - 4.5s): Gm7 (chromatic variation)
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # Bb4 (minor third)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=4.5),  # C4 (fifth)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=4.5),  # D4 (minor seventh)

    # Bar 4 (4.5 - 6.0s): Am7 (resolve)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=6.0),  # C5 (minor third)
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=6.0),  # E4 (fifth)
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=6.0),  # G4 (minor seventh)
]
piano.notes.extend(piano_notes)

# Drums - Bar 2-4
for bar in range(2, 5):
    start = bar * bar_length
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hats on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)
drums.notes.extend([note for note in drums.notes if note.start < 6.0])

# Sax - Dante (melody: one short motif, make it sing)
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F4

    # Bar 3: Continue motif
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # F4

    # Bar 4: Finish motif
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
