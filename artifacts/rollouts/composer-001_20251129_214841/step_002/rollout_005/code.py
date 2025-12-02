
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_kick)
drums.notes.append(drum_kick2)

# Snare on 2 and 4
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.append(drum_snare)
drums.notes.append(drum_snare2)

# Hi-hat on every eighth note
for i in range(0, 6, 1):
    start = i * 0.375
    end = start + 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: C7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 3: D7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: C7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: C (60) on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C (return)
]
sax.notes.extend(sax_notes)

# Bar 3: D (62) on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # A
]
sax.notes.extend(sax_notes)

# Bar 4: C (60) on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for i in range(2, 4):
    kick_start = i * 1.5
    kick_start2 = kick_start + 1.125
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=kick_start2, end=kick_start2 + 0.375)
    drums.notes.append(drum_kick)
    drums.notes.append(drum_kick2)

# Snare on 2 and 4
for i in range(2, 4):
    snare_start = i * 1.5 + 0.75
    snare_start2 = snare_start + 1.5
    drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=snare_start2, end=snare_start2 + 0.375)
    drums.notes.append(drum_snare)
    drums.notes.append(drum_snare2)

# Hi-hat on every eighth note
for i in range(0, 6, 1):
    start = 1.5 + i * 0.375
    end = start + 0.375
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
