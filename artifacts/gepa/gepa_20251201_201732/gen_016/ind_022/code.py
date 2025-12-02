
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0), # F2

    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375), # C3
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75), # E3
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # Eb3
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5), # C3

    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0), # F2
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, each bar a different chord
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=2.25), # F3
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=2.25), # A3
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25), # C4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # E4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=3.0), # Bb3
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=3.0), # D3
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0), # F3
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=3.0), # Ab3

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75), # C5
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)

# Sax: Dante, one short motif, start it, leave it hanging, come back and finish it
# Motif: F (G3) -> Bb (A3) -> C (Bb3?) -> F (D4) -> F (G3)
# Start on bar 2, end on bar 4

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # F4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875), # Bb3
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # G4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # F4
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0), # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
