
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Time signatures: 4/4, 1 bar = 1.5 seconds

# Bar 1: 0.0 - 1.5 seconds
# Drums only - kick on 1 and 3, snare on 2 and 4, hihat every eighth

# Create a kick on beat 1 (0.0s)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drums.notes.append(drum_note)

# Kick on beat 3 (1.125s)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_note)

# Snare on beat 2 (0.75s)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drums.notes.append(drum_note)

# Snare on beat 4 (1.5s)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
drums.notes.append(drum_note)

# Hi-hat every eighth note
for i in range(0, 6, 1):
    start = i * 0.375
    end = start + 0.375
    drum_note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(drum_note)

# Bar 2: 1.5 - 3.0 seconds (Full ensemble)
# Start with the sax melody in Dm (Dm7 -> G7 -> Cm7 -> F7)

# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

# sax melody: D -> F -> A -> D (held for 1.5 seconds)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)
sax.notes.append(sax_note)

# Bass line: walking line in Dm
# D - Eb - F - G (1.5 - 3.0s)
bass_note = pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=63, start=1.875, end=2.25)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=64, start=2.25, end=2.625)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=65, start=2.625, end=3.0)
bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (2.25s)
piano_note = pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625)
piano.notes.append(piano_note)

# G7 on 4 (3.0s)
piano_note = pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375)
piano.notes.append(piano_note)

# Bar 3: 3.0 - 4.5 seconds (Continue with the same pattern)
# Sax: F -> A -> D -> F (held for 1.5 seconds)
sax_note = pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5)
sax.notes.append(sax_note)

# Bass: walking line again
bass_note = pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=66, start=3.375, end=3.75)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=4.125)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=69, start=4.125, end=4.5)
bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
# Cm7 on 2 (3.75s)
piano_note = pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125)
piano.notes.append(piano_note)

# F7 on 4 (4.5s)
piano_note = pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875)
piano.notes.append(piano_note)

# Bar 4: 4.5 - 6.0 seconds (Finish the motif, leave it hanging)
# Sax: A -> D -> F -> stop
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0)
sax.notes.append(sax_note)

# Bass: walking again
bass_note = pretty_midi.Note(velocity=70, pitch=69, start=4.5, end=4.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=71, start=4.875, end=5.25)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=72, start=5.25, end=5.625)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=70, pitch=74, start=5.625, end=6.0)
bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
# Dm7 on 2 (5.25s)
piano_note = pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625)
piano.notes.append(piano_note)

# G7 on 4 (6.0s)
piano_note = pretty_midi.Note(velocity=80, pitch=67, start=6.0, end=6.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=71, start=6.0, end=6.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=72, start=6.0, end=6.375)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=80, pitch=74, start=6.0, end=6.375)
piano.notes.append(piano_note)

# Drums: same pattern
# Bar 3 (4.5 - 6.0s)
# Kick on 1 (4.5s), 3 (5.625s)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.append(drum_note)

# Snare on 2 (5.25s), 4 (6.0s)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)
drums.notes.append(drum_note)

# Hi-hat every eighth note in bar 3 and 4
for i in range(0, 6, 1):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drum_note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(drum_note)
for i in range(0, 6, 1):
    start = 6.0 + i * 0.375
    end = start + 0.375
    drum_note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(drum_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to disk
midi.write("dante_intro.mid")
