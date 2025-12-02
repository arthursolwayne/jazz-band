
import pretty_midi

# Initialize MIDI file with tempo 160 BPM and 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar (1.5 seconds)
BAR_DURATION = 1.5

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    # Bar 0 (time 0.0 to 1.5s)
    # Kick on 1 and 3 (beats 0 and 2)
    for kick_beat in [0, 2]:
        kick_time = kick_beat * BAR_DURATION / 4
        kick = pretty_midi.Note(velocity=100, pitch=KICK, start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick)
    
    # Snare on 2 and 4 (beats 1 and 3)
    for snare_beat in [1, 3]:
        snare_time = snare_beat * BAR_DURATION / 4
        snare = pretty_midi.Note(velocity=100, pitch=SNARE, start=snare_time, end=snare_time + 0.1)
        drums.notes.append(snare)
    
    # Hi-hat on every eighth note
    for eighth in range(8):
        hihat_time = eighth * BAR_DURATION / 8
        hihat = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start with D (D4), then F# (F#4), then B (B4), then rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
]

# Bass: walking line in D minor (D, Eb, F, G, A, Bb, B, C)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=70, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=70, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.5),  # G
]

# Piano: 7th chords on 2 and 4
# D7 (D, F#, A, C) - on beat 2 (1.75 - 2.0)
# Bm7 (B, D, F#, A) - on beat 4 (2.25 - 2.5)
piano_notes = []
# D7 on beat 2 (1.75 - 2.0)
for pitch in [62, 66, 69, 64]:  # D, F#, A, C
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=1.75, end=2.0))
# Bm7 on beat 4 (2.25 - 2.5)
for pitch in [71, 62, 66, 69]:  # B, D, F#, A
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=2.25, end=2.5))

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif, but with a slight variation (start with B, then D, then F#, then rest)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
]

# Bass: continue walking line
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=70, pitch=63, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=70, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=3.75, end=4.0),  # G
]

# Piano: 7th chords on 2 and 4
# B7 (B, D#, F#, A) - on beat 2 (3.25 - 3.5)
# Gm7 (G, Bb, D, F) - on beat 4 (3.75 - 4.0)
piano_notes = []
# B7 on beat 2 (3.25 - 3.5)
for pitch in [71, 67, 69, 69]:  # B, D#, F#, A
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=3.25, end=3.5))
# Gm7 on beat 4 (3.75 - 4.0)
for pitch in [67, 65, 62, 64]:  # G, Bb, D, F
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=3.75, end=4.0))

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif, bring it back to D, then rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D4
]

# Bass: continue walking line
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=70, pitch=63, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=70, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=5.25, end=5.5),  # G
]

# Piano: 7th chords on 2 and 4
# D7 on beat 2 (4.75 - 5.0)
# Bm7 on beat 4 (5.25 - 5.5)
piano_notes = []
# D7 on beat 2 (4.75 - 5.0)
for pitch in [62, 66, 69, 64]:  # D, F#, A, C
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=4.75, end=5.0))
# Bm7 on beat 4 (5.25 - 5.5)
for pitch in [71, 62, 66, 69]:  # B, D, F#, A
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=5.25, end=5.5))

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
