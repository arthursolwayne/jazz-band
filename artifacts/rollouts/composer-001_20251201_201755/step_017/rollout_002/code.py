
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0)   # F (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),   # Eb
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),   # Ab
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),   # F#
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0)    # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # G (Fm)
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # Bb (Fm)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625), # G (Fm)
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # E (Fm)
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # G (Fm)
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75), # C (Fm)
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # Bb (Fm)
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),  # G (Fm)
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # E (Fm)
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25), # G (Fm)
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625), # C (Fm)
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0)   # Bb (Fm)
]
sax.notes.extend(sax_notes)

# Bar 2: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
