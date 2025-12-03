
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875), # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625), # G (fifth)
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0), # G# (chromatic approach)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375), # G# (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75), # G (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125), # F (root)
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5), # D (chromatic approach)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875), # D (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # F (root)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # F# (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0), # G (fifth)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # E (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875), # C (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # A (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F (Fmaj7)

    # Bar 3: Bbm7 (Bb D F Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375), # Ab (Bbm7)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # D (Bbm7)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375), # F (Bbm7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # Bb (Bbm7)

    # Bar 4: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875), # F# (D7)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # A (D7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # C (D7)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # D (D7)
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F C E (F, C, E) on beat 1 of bar 2, leave it hanging on beat 2, return on beat 3
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0), # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5), # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0), # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
