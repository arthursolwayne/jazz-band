
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),  # Hihat on 1&2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),  # Hihat on 3&4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G2 on 3
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),   # Eb on 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # F on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # G2 on 3
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),   # Eb on 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # F on 2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # G2 on 3
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),   # Eb on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # Bb
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (D4), Eb (E4), D (D4), leave it hanging on Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D4 (return)
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on 1&2
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.75))
    # Kick on 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on 3&4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.5))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
