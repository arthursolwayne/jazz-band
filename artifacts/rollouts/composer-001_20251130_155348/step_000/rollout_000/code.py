
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - motif: D (D4), F# (F#4), B (B4), C# (C#5) - short, angular
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),
]

sax.notes.extend(sax_notes)

# Bass - walking line in D minor: D - C - B - A (downbeat to upbeat)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),   # A
]

bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4: D7 on 2, Bm7 on 4
piano_notes = [
    # D7 on 2 (beat 2, 1.875s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # B
    # Bm7 on 4 (beat 4, 2.625s)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # D
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - motif repeated, slightly delayed
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0),
])

# Bass - walking line: D - C - B - A (same pattern)
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),   # A
])

# Piano - 7th chords on 2 and 4: D7 on 2, Bm7 on 4 again
piano_notes.extend([
    # D7 on 2 (beat 2, 3.375s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # B
    # Bm7 on 4 (beat 4, 4.125s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # D
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - motif again, but ends on B (67) with a slight sustain
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.5),
])

# Bass - walking line again, ends on A (40)
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),   # A
])

# Piano - 7th chords on 2 and 4: D7 on 2, Bm7 on 4 again
piano_notes.extend([
    # D7 on 2 (beat 2, 4.875s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # B
    # Bm7 on 4 (beat 4, 5.625s)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # D
])

sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
