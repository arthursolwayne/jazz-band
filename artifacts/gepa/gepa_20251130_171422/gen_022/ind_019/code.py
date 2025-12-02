
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75)
hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375)
hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)
hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)
hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)

drums.notes.extend([kick1, snare1, hihat1, hihat2, hihat3, hihat4, kick2])

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # A
]

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # G
]

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),  # G
]

# Bar 3 (3.0 - 4.5s): Full quartet
# Bass: Walking line in F, chromatic approaches
bass_notes2 = [
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75), # D#
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),  # G
]

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes2 = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),  # G
]

# Sax: Motif continuation
sax_notes2 = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G#
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5),  # G
]

# Bar 4 (4.5 - 6.0s): Full quartet
# Bass: Walking line in F, chromatic approaches
bass_notes3 = [
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25), # G#
    pretty_midi.Note(velocity=80, pitch=79, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),  # B
]

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes3 = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # G
]

# Sax: Motif completion
sax_notes3 = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=6.0),  # G
]

# Add notes to instruments
bass.notes.extend(bass_notes + bass_notes2 + bass_notes3)
piano.notes.extend(piano_notes + piano_notes2 + piano_notes3)
sax.notes.extend(sax_notes + sax_notes2 + sax_notes3)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=90, pitch=38, start=start + 0.375, end=start + 0.75)
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat1, hihat2, hihat3, hihat4, kick2])

midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.save('dante_intro.mid')
