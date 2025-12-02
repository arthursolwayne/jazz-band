
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
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
# F7 chord: F A C E (root, 3, 5, 7)
# We walk F, G#, Bb, B, C#, D, E, F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=80, pitch=73, start=3.0, end=3.375),  # C#
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=73, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=80, pitch=73, start=5.625, end=6.0),  # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 = F A C E
# Comp on beat 2 and 4 of each bar
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2: F7 comp on beat 2 (start + 0.75)
    for note in [71, 74, 76, 79]:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + 0.75, end=start + 1.125))
    # Bar 3: F7 comp on beat 2 (start + 0.75)
    for note in [71, 74, 76, 79]:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + 0.75, end=start + 1.125))
    # Bar 4: F7 comp on beat 2 (start + 0.75)
    for note in [71, 74, 76, 79]:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start + 0.75, end=start + 1.125))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on beat 0 and 2
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 1 and 3
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G#, Bb, C, B, A, G#, F – F minor pentatonic with some tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.6875, end=1.875),  # G#
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.0625, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.4375, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=2.625, end=2.8125),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=2.8125, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=3.9375, end=4.125),  # G#
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.3125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.3125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.6875),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.0625),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=5.0625, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=5.4375, end=5.625),  # G#
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=5.8125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.8125, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
