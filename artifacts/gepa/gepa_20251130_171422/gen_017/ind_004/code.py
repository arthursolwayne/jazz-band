
import pretty_midi

# Initialize the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Question: A kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
# Let the hihat breathe, and make the kick and snare feel like a question.

# Kick on 1 and 3 (160 BPM = 0.375s per beat)
drum_kick1 = pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125)

# Snare on 2 and 4
drum_snare1 = pretty_midi.Note(velocity=110, pitch=SNARE, start=0.375, end=0.75)
drum_snare2 = pretty_midi.Note(velocity=110, pitch=SNARE, start=1.125, end=1.5)

# Hi-hat on every eighth note (0.375s intervals)
hihat_notes = [0.0, 0.375, 0.75, 1.125]
for time in hihat_notes:
    hihat = pretty_midi.Note(velocity=80, pitch=HIHAT, start=time, end=time + 0.375)
    drums.notes.append(hihat)

drums.notes.extend([drum_kick1, drum_kick2, drum_snare1, drum_snare2])

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: F#7 (D7 chord), then D#7 (G7 chord), then B7 (B7), then rest.
# Melody is a question — a phrase that doesn't resolve but lingers.

# D7 chord (F#, A#, D, F#)
sax_note1 = pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75)  # F#
sax_note2 = pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0)  # A#
sax_note3 = pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25)  # D
sax_note4 = pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5)  # F#
sax_note5 = pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75)  # D#
sax_note6 = pretty_midi.Note(velocity=110, pitch=76, start=2.75, end=3.0)  # G
sax_note7 = pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.25)  # B
sax_note8 = pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5)  # B

# Bass line (Walking line, chromatic approaches)
# D - C# - B - C - D
bass_note1 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75)  # D
bass_note2 = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0)  # C#
bass_note3 = pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25)  # B
bass_note4 = pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5)  # C
bass_note5 = pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75)  # D
bass_note6 = pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0)  # C
bass_note7 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25)  # B
bass_note8 = pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5)  # D

# Piano: 7th chords, comp on 2 and 4 (D7 on 2, G7 on 4)
# D7: F#, A#, D, C
# G7: B, D, F#, G
# D7 on 2 (1.75-2.0), G7 on 4 (2.75-3.0)
piano_note1 = pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0)  # F#
piano_note2 = pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0)  # A#
piano_note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0)  # D
piano_note4 = pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0)  # C

piano_note5 = pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0)  # B
piano_note6 = pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0)  # D
piano_note7 = pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0)  # F#
piano_note8 = pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0)  # G

# Bar 3: Continue the quartet (3.0 - 4.5s)
# Saxophone: repeat the motif but with a variation — end on B and hold it
# D7 and G7 again, but with a little push

# Saxophone motif variation
sax_note9 = pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25)  # F#
sax_note10 = pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5)  # A#
sax_note11 = pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75)  # D
sax_note12 = pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0)  # F#
sax_note13 = pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25)  # D#
sax_note14 = pretty_midi.Note(velocity=110, pitch=76, start=4.25, end=4.5)  # G
sax_note15 = pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=5.0)  # B (hold)

# Bass walking line continues
bass_note9 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25)  # D
bass_note10 = pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5)  # C#
bass_note11 = pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75)  # B
bass_note12 = pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0)  # C
bass_note13 = pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25)  # D
bass_note14 = pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5)  # C
bass_note15 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75)  # B
bass_note16 = pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0)  # D

# Piano: D7 on 2, G7 on 4 (same as before, but slightly louder)
piano_note9 = pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5)  # F#
piano_note10 = pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5)  # A#
piano_note11 = pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5)  # D
piano_note12 = pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5)  # C

piano_note13 = pretty_midi.Note(velocity=110, pitch=71, start=4.25, end=4.5)  # B
piano_note14 = pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5)  # D
piano_note15 = pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5)  # F#
piano_note16 = pretty_midi.Note(velocity=110, pitch=71, start=4.25, end=4.5)  # G

# Bar 4: Continue the quartet (4.5 - 6.0s)
# Saxophone: End with a rest, but leave the B hanging. Resolution is implied, not stated.
# D7 on 2, G7 on 4 (same pattern)

# Saxophone: Rest for the first half, then end on B with a slight release
sax_note17 = pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=5.0)  # B (hold)

# Bass: Continue walking line to the end
bass_note17 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75)  # D
bass_note18 = pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0)  # C#

# Piano: D7 on 2 (4.75-5.0)
piano_note17 = pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0)  # F#
piano_note18 = pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0)  # A#
piano_note19 = pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0)  # D
piano_note20 = pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0)  # C

# Add all the notes to their respective instruments
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4, sax_note5, sax_note6, sax_note7, sax_note8, sax_note9, sax_note10, sax_note11, sax_note12, sax_note13, sax_note14, sax_note15, sax_note17])
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4, bass_note5, bass_note6, bass_note7, bass_note8, bass_note9, bass_note10, bass_note11, bass_note12, bass_note13, bass_note14, bass_note15, bass_note16, bass_note17, bass_note18])
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4, piano_note5, piano_note6, piano_note7, piano_note8, piano_note9, piano_note10, piano_note11, piano_note12, piano_note13, piano_note14, piano_note15, piano_note16, piano_note17, piano_note18, piano_note19, piano_note20])

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
