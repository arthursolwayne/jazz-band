
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)  # Snare on 4 (outside bar)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (F, Bb, B, Ab, F, Bb, B, Ab)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 (bar 2, beat 1)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Bb2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # B2 (beat 3)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # Ab2 (beat 4)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # F2 (bar 3, beat 1)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # Bb2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # B2 (beat 3)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # Ab2 (beat 4)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F2 (bar 4, beat 1)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # Bb2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # B2 (beat 3)
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # Ab2 (beat 4)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),   # F4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),   # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),   # C4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),   # E4
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=3.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),   # D4
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=3.0),   # F4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),   # Ab4
])
# Bar 4: F7 (F, A, C, Eb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),   # F4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),   # A4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),   # C4
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.75),   # Eb4
])
# Bar 4 resolution: Fmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.5),   # F4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5),   # A4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5),   # C4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5),   # E4
])
piano.notes.extend(piano_notes)

# Dante: Sax - One short motif, make it sing. Start, leave it hanging, return and finish it.
# Motif: F, G, Bb, F (3 notes, leave the 4th hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),   # F5
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # G5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb5
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # F5 (left hanging)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),   # F5 (return)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # G5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb5
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # F5 (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1 (bar 2)
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),   # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1 (bar 3)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),   # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3 (bar 4)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
