
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.

# Create notes for bar 1
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=90, pitch=36, start=bar1_start + 0.0, end=bar1_start + 0.0 + 0.375)
kick2 = pretty_midi.Note(velocity=90, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.125 + 0.375)
drums.notes.append(kick1)
drums.notes.append(kick2)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.5 - 0.375, end=bar1_start + 1.5)
drums.notes.append(snare1)
drums.notes.append(snare2)

# Hi-hat on every eighth
hihat_notes = [bar1_start + i * 0.375 for i in range(4)]
for start in hihat_notes:
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125)
    drums.notes.append(hihat)

# Bar 2 (1.5 - 3.0s)
# Saxophone: short motif, start it, leave it hanging

bar2_start = 1.5
bar2_end = 3.0

# Saxophone: Dm7 chord tones (D, F, A, C), with syncopation
# Motif: D, F, A, rest
sax_note1 = pretty_midi.Note(velocity=110, pitch=62, start=bar2_start + 0.0, end=bar2_start + 0.25)
sax_note2 = pretty_midi.Note(velocity=110, pitch=64, start=bar2_start + 0.5, end=bar2_start + 0.75)
sax_note3 = pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 1.0, end=bar2_start + 1.25)
sax.notes.append(sax_note1)
sax.notes.append(sax_note2)
sax.notes.append(sax_note3)

# Bass: walking line in Dm, chromatic approach to F
bass_note1 = pretty_midi.Note(velocity=80, pitch=43, start=bar2_start, end=bar2_start + 0.375)  # D
bass_note2 = pretty_midi.Note(velocity=80, pitch=44, start=bar2_start + 0.375, end=bar2_start + 0.75)  # Eb
bass_note3 = pretty_midi.Note(velocity=80, pitch=45, start=bar2_start + 0.75, end=bar2_start + 1.125)  # E
bass_note4 = pretty_midi.Note(velocity=80, pitch=46, start=bar2_start + 1.125, end=bar2_start + 1.5)  # F
bass.notes.append(bass_note1)
bass.notes.append(bass_note2)
bass.notes.append(bass_note3)
bass.notes.append(bass_note4)

# Piano: 7th chords on 2 and 4, comp
piano_note1 = pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 0.75, end=bar2_start + 1.125)  # D7
piano_note2 = pretty_midi.Note(velocity=90, pitch=64, start=bar2_start + 0.75, end=bar2_start + 1.125)
piano_note3 = pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125)
piano_note4 = pretty_midi.Note(velocity=90, pitch=71, start=bar2_start + 0.75, end=bar2_start + 1.125)
piano.notes.append(piano_note1)
piano.notes.append(piano_note2)
piano.notes.append(piano_note3)
piano.notes.append(piano_note4)

# Bar 3 (3.0 - 4.5s)
# Saxophone: rest, then answer with a variation
bar3_start = 3.0
bar3_end = 4.5

# Saxophone: rest at first half, then variation
sax_note4 = pretty_midi.Note(velocity=110, pitch=67, start=bar3_start + 0.5, end=bar3_start + 0.75)
sax_note5 = pretty_midi.Note(velocity=110, pitch=64, start=bar3_start + 1.0, end=bar3_start + 1.25)
sax_note6 = pretty_midi.Note(velocity=110, pitch=62, start=bar3_start + 1.5, end=bar3_start + 1.75)
sax.notes.append(sax_note4)
sax.notes.append(sax_note5)
sax.notes.append(sax_note6)

# Bass: walking line in Dm, chromatic approach to A
bass_note5 = pretty_midi.Note(velocity=80, pitch=46, start=bar3_start, end=bar3_start + 0.375)  # F
bass_note6 = pretty_midi.Note(velocity=80, pitch=47, start=bar3_start + 0.375, end=bar3_start + 0.75)  # F#
bass_note7 = pretty_midi.Note(velocity=80, pitch=48, start=bar3_start + 0.75, end=bar3_start + 1.125)  # G
bass_note8 = pretty_midi.Note(velocity=80, pitch=50, start=bar3_start + 1.125, end=bar3_start + 1.5)  # A
bass.notes.append(bass_note5)
bass.notes.append(bass_note6)
bass.notes.append(bass_note7)
bass.notes.append(bass_note8)

# Piano: 7th chords on 2 and 4, comp
piano_note5 = pretty_midi.Note(velocity=90, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125)  # D7
piano_note6 = pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + 0.75, end=bar3_start + 1.125)
piano_note7 = pretty_midi.Note(velocity=90, pitch=72, start=bar3_start + 0.75, end=bar3_start + 1.125)
piano_note8 = pretty_midi.Note(velocity=90, pitch=76, start=bar3_start + 0.75, end=bar3_start + 1.125)
piano.notes.append(piano_note5)
piano.notes.append(piano_note6)
piano.notes.append(piano_note7)
piano.notes.append(piano_note8)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick3 = pretty_midi.Note(velocity=90, pitch=36, start=bar3_start + 0.0, end=bar3_start + 0.0 + 0.375)
kick4 = pretty_midi.Note(velocity=90, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.125 + 0.375)
drums.notes.append(kick3)
drums.notes.append(kick4)

# Snare on 2 and 4
snare3 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375)
snare4 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 1.5 - 0.375, end=bar3_start + 1.5)
drums.notes.append(snare3)
drums.notes.append(snare4)

# Hi-hat on every eighth
hihat_notes = [bar3_start + i * 0.375 for i in range(4)]
for start in hihat_notes:
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125)
    drums.notes.append(hihat)

# Bar 4 (4.5 - 6.0s)
# Saxophone: finish the motif, leave it hanging
bar4_start = 4.5
bar4_end = 6.0

# Saxophone: finish with a rest on the last eighth
sax_note7 = pretty_midi.Note(velocity=110, pitch=62, start=bar4_start + 0.0, end=bar4_start + 0.25)
sax_note8 = pretty_midi.Note(velocity=110, pitch=64, start=bar4_start + 0.5, end=bar4_start + 0.75)
sax_note9 = pretty_midi.Note(velocity=110, pitch=67, start=bar4_start + 1.0, end=bar4_start + 1.25)
sax.notes.append(sax_note7)
sax.notes.append(sax_note8)
sax.notes.append(sax_note9)

# Bass: walking line in Dm, chromatic approach to C
bass_note9 = pretty_midi.Note(velocity=80, pitch=50, start=bar4_start, end=bar4_start + 0.375)  # A
bass_note10 = pretty_midi.Note(velocity=80, pitch=51, start=bar4_start + 0.375, end=bar4_start + 0.75)  # A#
bass_note11 = pretty_midi.Note(velocity=80, pitch=52, start=bar4_start + 0.75, end=bar4_start + 1.125)  # B
bass_note12 = pretty_midi.Note(velocity=80, pitch=53, start=bar4_start + 1.125, end=bar4_start + 1.5)  # C
bass.notes.append(bass_note9)
bass.notes.append(bass_note10)
bass.notes.append(bass_note11)
bass.notes.append(bass_note12)

# Piano: 7th chords on 2 and 4, comp
piano_note9 = pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + 0.75, end=bar4_start + 1.125)  # D7
piano_note10 = pretty_midi.Note(velocity=90, pitch=64, start=bar4_start + 0.75, end=bar4_start + 1.125)
piano_note11 = pretty_midi.Note(velocity=90, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125)
piano_note12 = pretty_midi.Note(velocity=90, pitch=71, start=bar4_start + 0.75, end=bar4_start + 1.125)
piano.notes.append(piano_note9)
piano.notes.append(piano_note10)
piano.notes.append(piano_note11)
piano.notes.append(piano_note12)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick5 = pretty_midi.Note(velocity=90, pitch=36, start=bar4_start + 0.0, end=bar4_start + 0.0 + 0.375)
kick6 = pretty_midi.Note(velocity=90, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.125 + 0.375)
drums.notes.append(kick5)
drums.notes.append(kick6)

# Snare on 2 and 4
snare5 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375)
snare6 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.5 - 0.375, end=bar4_start + 1.5)
drums.notes.append(snare5)
drums.notes.append(snare6)

# Hi-hat on every eighth
hihat_notes = [bar4_start + i * 0.375 for i in range(4)]
for start in hihat_notes:
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.125)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
