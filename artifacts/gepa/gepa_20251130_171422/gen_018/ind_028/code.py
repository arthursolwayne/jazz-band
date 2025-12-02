
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

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_3])

# Snare on 2 and 4
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.extend([drum_snare_2, drum_snare_4])

# Hi-hat on every eighth note
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=5.75, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # F7 - D
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Bb7 - Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # Bb7 - D
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # Bb7 - F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),  # Bb7 - Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # F7 - D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # Bb7 - Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # Bb7 - D
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # Bb7 - F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # Bb7 - Ab
]
piano.notes.extend(diane_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):
    start = i * 1.5
    drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    drums.notes.extend([drum_kick_1, drum_kick_3, drum_snare_2, drum_snare_4, drum_hihat])

# Dante: Tenor sax motif (start at bar 2)
# Motif: Dm7 -> G7 -> Cm7 -> F7
# Dm7: D - F - A - C (octave adjusted)
# G7: G - B - D - F
# Cm7: C - Eb - G - Bb
# F7: F - A - C - Eb

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # C
]

# Bar 3 (G7)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # F
])

# Bar 4 (Cm7)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # Bb
])

# Bar 4 (F7)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # Eb
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
