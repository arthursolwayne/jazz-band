
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
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([kick1, kick2])

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0)
drums.notes.extend([snare1, snare2])

# Hi-hat on every eighth
hihat_notes = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for t in hihat_notes:
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.125)
    drums.notes.append(hihat)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Marcus, walking line in Fm, chromatic approaches
# Fm = F, Ab, Bb, D
# Chromatic approaches below each note

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.5),  # D

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # Db
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # Eb

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),  # Db
    pretty_midi.Note(velocity=90, pitch=61, start=4.25, end=4.5),  # C

    # Bar 4 continuation
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, C
# Comp on 2 and 4

piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # C

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # C

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # C
]
piano.notes.extend(piano_notes)

# Sax: Dante, short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start of motif
# F, Gb, Ab, Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),  # Bb

    # Bar 3: Silence
    # Leave it hanging

    # Bar 4: Return and finish
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
# Kick on 1 and 3
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75)
kick5 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drums.notes.extend([kick3, kick4, kick5])

# Snare on 2 and 4
snare3 = pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75)
snare4 = pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875)
snare5 = pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0)
drums.notes.extend([snare3, snare4, snare5])

# Hi-hat on every eighth
hihat_notes = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
for t in hihat_notes:
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.125)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
