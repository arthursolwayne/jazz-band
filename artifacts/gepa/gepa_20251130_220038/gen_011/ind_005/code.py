
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

kick1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick1, snare1, hihat1])

# Bar 2: Full quartet (1.5 - 3.0s)

# Drums
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick2, snare2, hihat2])

# Bass (Marcus) - walking line with chromatic approaches
# F7 chord: F, A, C, E
# Walking line: F, G#, A, Bb (chromatic approach to Bb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.75, end=2.0),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
# F7 on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=2.75, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax (Dante) - one short motif, make it sing
# F, G, Bb, A (F7 with a tritone substitution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick3, snare3, hihat3])

# Bass (Marcus) - walking line
# F, Eb, D, C (chromatic approach to C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
# F7 on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=4.25, end=4.5),  # E
]
piano.notes.extend(piano_notes)

# Sax (Dante) - repeat motif with variation
# F, G, Bb, Ab (tritone substitution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # Ab
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick4, snare4, hihat4])

# Bass (Marcus) - walking line
# F, Eb, D, C (chromatic approach to C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
# F7 on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=5.75, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Sax (Dante) - repeat motif with resolution
# F, G, Bb, C (resolve to C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
