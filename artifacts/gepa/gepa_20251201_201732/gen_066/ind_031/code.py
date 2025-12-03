
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

# Bass line - Marcus: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=75, start=1.875, end=2.25), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # E (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # F (root)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Bb (fourth)
    pretty_midi.Note(velocity=100, pitch=78, start=3.375, end=3.75), # D (fifth)
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125), # C# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5),  # D (fifth)
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=75, start=4.875, end=5.25), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # E (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),  # F (root)
]
bass.notes.extend(bass_notes)

# Piano - Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),
]
# Bar 3: Bbmaj7 (Bb, D, F, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625),
])
# Bar 4: D7 (D, F#, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),
])
# Resolving chord on last bar (Fmaj7)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),
])
piano.notes.extend(piano_notes)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (70) - A (74) - F (70) - Bb (72)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=74, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=70, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=2.875),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
