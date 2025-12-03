
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
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=75, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25), # G (fifth)
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625), # F# (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=75, start=2.625, end=3.0),  # F (root)
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # A (root of next chord)
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.75), # B (fifth)
    pretty_midi.Note(velocity=90, pitch=80, start=3.75, end=4.125), # A# (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),  # A (root)
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.875),  # B (root of next chord)
    pretty_midi.Note(velocity=90, pitch=84, start=4.875, end=5.25), # C# (fifth)
    pretty_midi.Note(velocity=90, pitch=83, start=5.25, end=5.625), # C (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=82, start=5.625, end=6.0)   # B (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 - Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=75, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=85, start=1.5, end=1.875),
    # Bar 3 - Amaj7 (A, C#, E, G#)
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=83, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=86, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=89, start=2.25, end=2.625),
    # Bar 4 - B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=86, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=89, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=91, start=3.0, end=3.375),
    # Resolving chords for each bar
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75),  # F (resolves bar 2)
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125),  # A (resolves bar 3)
    pretty_midi.Note(velocity=90, pitch=82, start=4.125, end=4.5),   # B (resolves bar 4)
    pretty_midi.Note(velocity=90, pitch=85, start=4.5, end=4.875),  # F (resolves bar 2 again)
    pretty_midi.Note(velocity=90, pitch=86, start=4.875, end=5.25),  # C# (resolves bar 3 again)
    pretty_midi.Note(velocity=90, pitch=91, start=5.25, end=5.625), # A (resolves bar 4 again)
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),   # G
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=80, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=5.0, end=5.25),   # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.75, end=6.0)    # Bb
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
