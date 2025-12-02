
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
bar1_start = 0.0
bar1_end = 1.5
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375)
hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=bar1_start, end=bar1_end)
drums.notes.extend([kick1, snare1, hihat1])

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Marcus: Walking bass line in Dm (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=bar2_start, end=bar2_start + 0.375), # F
    pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 0.375, end=bar2_start + 0.75), # G
    pretty_midi.Note(velocity=80, pitch=72, start=bar2_start + 0.75, end=bar2_start + 1.125), # A
    pretty_midi.Note(velocity=80, pitch=70, start=bar2_start + 1.125, end=bar2_end), # F
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
# Dm7 = D, F, A, C (pitches 62, 65, 67, 69)
# Bar 2, beat 2 (0.75s into bar2)
diane_note_1 = pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 0.75, end=bar2_start + 1.125)
diane_note_2 = pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 0.75, end=bar2_start + 1.125)
diane_note_3 = pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125)
diane_note_4 = pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + 0.75, end=bar2_start + 1.125)
piano.notes.extend([diane_note_1, diane_note_2, diane_note_3, diane_note_4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.75 + 0.375)
hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=bar2_start, end=bar2_end)
drums.notes.extend([kick2, snare2, hihat2])

# Dante: Tenor sax motif - start with a short phrase that sings
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62), F (65), Bb (67), G (67) - ascending with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 1.125, end=bar2_end),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=bar3_start, end=bar3_start + 0.375), # F
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start + 0.375, end=bar3_start + 0.75), # G
    pretty_midi.Note(velocity=80, pitch=72, start=bar3_start + 0.75, end=bar3_start + 1.125), # A
    pretty_midi.Note(velocity=80, pitch=70, start=bar3_start + 1.125, end=bar3_end), # F
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
# Dm7 = D, F, A, C (pitches 62, 65, 67, 69)
# Bar 3, beat 2 (0.75s into bar3)
diane_note_1 = pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + 0.75, end=bar3_start + 1.125)
diane_note_2 = pretty_midi.Note(velocity=90, pitch=65, start=bar3_start + 0.75, end=bar3_start + 1.125)
diane_note_3 = pretty_midi.Note(velocity=90, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125)
diane_note_4 = pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + 0.75, end=bar3_start + 1.125)
piano.notes.extend([diane_note_1, diane_note_2, diane_note_3, diane_note_4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick3 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375)
hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=bar3_start, end=bar3_end)
drums.notes.extend([kick3, snare3, hihat3])

# Dante: Tenor sax motif - continue the phrase from bar 2, with a twist
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62), F (65), Bb (67), G (67) - ascending with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=65, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=67, start=bar3_start + 1.125, end=bar3_end),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=bar4_start, end=bar4_start + 0.375), # F
    pretty_midi.Note(velocity=80, pitch=71, start=bar4_start + 0.375, end=bar4_start + 0.75), # G
    pretty_midi.Note(velocity=80, pitch=72, start=bar4_start + 0.75, end=bar4_start + 1.125), # A
    pretty_midi.Note(velocity=80, pitch=70, start=bar4_start + 1.125, end=bar4_end), # F
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
# Dm7 = D, F, A, C (pitches 62, 65, 67, 69)
# Bar 4, beat 2 (0.75s into bar4)
diane_note_1 = pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + 0.75, end=bar4_start + 1.125)
diane_note_2 = pretty_midi.Note(velocity=90, pitch=65, start=bar4_start + 0.75, end=bar4_start + 1.125)
diane_note_3 = pretty_midi.Note(velocity=90, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125)
diane_note_4 = pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + 0.75, end=bar4_start + 1.125)
piano.notes.extend([diane_note_1, diane_note_2, diane_note_3, diane_note_4])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick4 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375)
hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=bar4_start, end=bar4_end)
drums.notes.extend([kick4, snare4, hihat4])

# Dante: Tenor sax motif - finish the phrase, leave it hanging
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62), F (65), Bb (67), G (67) - ascending with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=65, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 1.125, end=bar4_end),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
