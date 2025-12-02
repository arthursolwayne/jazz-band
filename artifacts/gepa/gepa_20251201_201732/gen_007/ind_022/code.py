
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i in range(2):
    kick_time = 0.0 + i * 1.5
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    kick_notes[i] = kick_note

for i in range(2):
    snare_time = 0.75 + i * 1.5
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.375)
    snare_notes[i] = snare_note

for i in range(8):
    hihat_time = i * 0.375
    hihat_note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125)
    hihat_notes[i] = hihat_note

drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)
drums.notes.extend(hihat_notes)

# Bar 2: Full quartet
# Bass: walking line, roots and fifths with chromatic approaches
# Dm - F - A - C
bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875))  # D
bass_notes.append(pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25)) # C
bass_notes.append(pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625)) # F
bass_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0))  # F#

bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 - G7 - Cm7 - F7
piano_notes = []
# Dm7
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)) # D
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)) # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0)) # Bb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0)) # F

piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing
# Start with D, Bb, F - leave hanging
sax_notes = []
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)) # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25)) # G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625)) # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0)) # Bb

sax.notes.extend(sax_notes)

# Bar 3: Full quartet
# Bass: walking line
bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))  # G
bass_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75)) # F
bass_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125)) # C
bass_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5))  # C#

bass.notes.extend(bass_notes)

# Piano: G7
piano_notes = []
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)) # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5)) # B
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5)) # A
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5)) # F

piano.notes.extend(piano_notes)

# Sax: repeat motif but resolve
sax_notes = []
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375)) # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75)) # G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125)) # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5)) # Bb

sax.notes.extend(sax_notes)

# Bar 4: Full quartet
# Bass: walking line
bass_notes = []
bass_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875))  # F
bass_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)) # D
bass_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625)) # C
bass_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0))  # C#

bass.notes.extend(bass_notes)

# Piano: Cm7
piano_notes = []
piano_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0)) # C
piano_notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0)) # Eb
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)) # G
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)) # Bb

piano.notes.extend(piano_notes)

# Sax: resolve the motif
sax_notes = []
sax_notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875)) # D
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25)) # G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625)) # F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0)) # Bb

sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i in range(2):
    kick_time = 3.0 + i * 1.5
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.375)
    kick_notes[i] = kick_note

for i in range(2):
    snare_time = 3.75 + i * 1.5
    snare_note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.375)
    snare_notes[i] = snare_note

for i in range(8):
    hihat_time = 3.0 + i * 0.375
    hihat_note = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.125)
    hihat_notes[i] = hihat_note

drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)
drums.notes.extend(hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
