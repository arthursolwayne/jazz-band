
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

kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)

drums.notes.extend([kick, snare, hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # Gb2
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),  # Gb2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),  # Eb4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=3.0),  # F5
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=3.0),  # Ab5
])
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.75),  # Db4
])
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25)
drums.notes.extend([kick, snare, hihat])

# Bar 3
kick = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
snare = pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0)
drums.notes.extend([kick, snare, hihat])

# Bar 4
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75)
drums.notes.extend([kick, snare, hihat])

# Dante: Tenor sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=2.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=63, start=5.0, end=5.25),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=63, start=5.5, end=5.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
