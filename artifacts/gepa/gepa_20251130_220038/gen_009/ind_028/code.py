
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C
]
piano.notes.extend(piano_notes)

# Drums: same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody in Dm: Dm7 -> Eb7 -> F7 -> Gm7
# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
