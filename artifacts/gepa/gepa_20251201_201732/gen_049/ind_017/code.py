
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums

# Kick on 1 and 3
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_note)

# Snare on 2 and 4
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0)
drums.notes.append(drum_note)

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drum_note = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) on beat 1, F#2 (MIDI 41) on beat 2, A2 (MIDI 45) on beat 3, C#3 (MIDI 48) on beat 4
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0)
bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0)
piano.notes.append(piano_note)

# Sax: Motif - D4 (MIDI 62) on beat 1, F#4 (MIDI 67) on beat 2, A4 (MIDI 71) on beat 3, rest on beat 4
sax_note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625)
sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) on beat 1, A2 (MIDI 45) on beat 2, D3 (MIDI 50) on beat 3, F#3 (MIDI 53) on beat 4
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5)
bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar
# Bar 3: D7 (D-F#-A-C)
piano_note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5)
piano.notes.append(piano_note)

# Sax: Motif continuation - C#4 (MIDI 70) on beat 1, rest on beats 2-4
sax_note = pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375)
sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) on beat 1, F#2 (MIDI 41) on beat 2, A2 (MIDI 45) on beat 3, D3 (MIDI 50) on beat 4
bass_note = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0)
bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar
# Bar 4: Dmin7 (D-F-A-C)
piano_note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0)
piano.notes.append(piano_note)
piano_note = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0)
piano.notes.append(piano_note)

# Sax: Motif finish - D4 (MIDI 62) on beat 1, rest on beats 2-4
sax_note = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875)
sax.notes.append(sax_note)

# Drums: Bar 4
# Kick on 1 and 3
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drums.notes.append(drum_note)

# Snare on 2 and 4
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0)
drums.notes.append(drum_note)
drum_note = pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0)
drums.notes.append(drum_note)

# Hihat on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drum_note = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
