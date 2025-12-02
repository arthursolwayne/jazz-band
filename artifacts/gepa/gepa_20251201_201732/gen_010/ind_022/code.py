
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
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, roots and fifths, with chromatic approaches
bass_notes = [
    # Bar 2: F (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),

    # Bar 3: C (fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5),

    # Bar 4: F (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),

    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, snare2, hihat, kick3, snare4])

# Saxophone: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F, played on beat 1 of bar 2, then repeated on beat 1 of bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.875, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.375),  # F

    # Repeat on beat 1 of bar 4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875)   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
