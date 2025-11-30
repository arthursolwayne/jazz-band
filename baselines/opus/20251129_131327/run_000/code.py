
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42
KICK, SNARE, HIHAT = 36, 38, 42
BEAT = 0.375  # 160 BPM

# Key of Eb minor. Wayne's territory. Show respect, then take it somewhere.

# === BAR 1: Little Ray alone (0.0 - 1.5s) ===
# Set it up. Make them wait. Tension in the silence.
for i in range(8):  # Eighth note hihats
    drums.notes.append(pretty_midi.Note(velocity=70 if i % 2 == 0 else 50, pitch=HIHAT, 
                                         start=i * BEAT/2, end=i * BEAT/2 + 0.1))
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0, end=0.2))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=KICK, start=BEAT*2, end=BEAT*2 + 0.2))
# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=BEAT, end=BEAT + 0.15))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=BEAT*3, end=BEAT*3 + 0.15))

# === BARS 2-4: Full quartet (1.5 - 6.0s) ===

# Continue drums pattern for bars 2-4
for bar in range(1, 4):
    bar_start = bar * 1.5
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=70 if i % 2 == 0 else 50, pitch=HIHAT,
                                             start=bar_start + i * BEAT/2, end=bar_start + i * BEAT/2 + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start, end=bar_start + 0.2))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=KICK, start=bar_start + BEAT*2, end=bar_start + BEAT*2 + 0.2))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=bar_start + BEAT, end=bar_start + BEAT + 0.15))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=bar_start + BEAT*3, end=bar_start + BEAT*3 + 0.15))

# Marcus - walking bass. Eb minor. Chromatic approaches. Never the same note twice.
# Eb3=51, Gb3=54, Ab3=56, Bb3=58, Db4=61, Cb3=59, A3=57, E3=52
marcus_line = [
    (1.5, 51, 0.35),   # Eb - root, statement
    (1.875, 57, 0.35), # A - tritone sub approach
    (2.25, 58, 0.35),  # Bb - the 5
    (2.625, 61, 0.35), # Db - climbing
    (3.0, 54, 0.35),   # Gb - drop down, minor 3rd
    (3.375, 52, 0.35), # E - chromatic approach from below
    (3.75, 56, 0.35),  # Ab - 4
    (4.125, 59, 0.35), # B natural - tension
    (4.5, 51, 0.35),   # Eb - home
    (4.875, 53, 0.35), # F - chromatic up
    (5.25, 54, 0.35),  # Gb - minor 3rd
    (5.625, 49, 0.35), # Db - drop, leading back
]
for start, pitch, dur in marcus_line:
    bass.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=start + dur))

# Diane - 7th chords, comp on 2 and 4. Angry but controlled.
# Ebm7: Eb4-Gb4-Bb4-Db5 = 63-66-70-73
# Abm7: Ab3-Cb4-Eb4-Gb4 = 56-59-63-66
# Bbm7: Bb3-Db4-F4-Ab4 = 58-61-65-68
diane_voicings = [
    # Bar 2: Ebm7 on 2 and 4
    (1.875, [66, 70, 73], 0.3),      # Ebm7 shell - beat 2
    (2.625, [63, 66, 73], 0.25),     # Ebm7 inversion - beat 4
    # Bar 3: Abm7 tension
    (3.375, [59, 63, 68], 0.3),      # Abm7 - beat 2
    (4.125, [61, 65, 70], 0.25),     # Bbm7 - beat 4, push forward
    # Bar 4: resolve and suspend
    (4.875, [66, 70, 75], 0.3),      # Ebm9 - beat 2, open it up
    (5.625, [63, 68, 73], 0.35),     # suspended, unresolved - beat 4
]
for start, pitches, dur in diane_voicings:
    for p in pitches:
        piano.notes.append(pretty_midi.Note(velocity=70, pitch=p, start=start, end=start + dur))

# Dante - the sax. One motif. Start it. Leave it hanging. Come back. Finish it.
# The motif: Bb5 down to Gb5, hang on Db5. That's the question.
# The answer: Start on Db5, climb to Eb5, fall to Bb4. That's the memory walking through the door.

# Bar 2: The question - comes in on the and of 2
sax.notes.append(pretty_midi.Note(velocity=95, pitch=82, start=2.0, end=2.25))    # Bb5 - cry
sax.notes.append(pretty_midi.Note(velocity=85, pitch=78, start=2.3, end=2.55))    # Gb5 - fall
sax.notes.append(pretty_midi.Note(velocity=80, pitch=73, start=2.6, end=3.2))     # Db5 - hang... let it breathe

# Bar 3: Silence. Let them wonder. Just a ghost note.
sax.notes.append(pretty_midi.Note(velocity=50, pitch=70, start=3.9, end=4.05))    # Bb4 - whisper

# Bar 4: The answer - you come back
sax.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=4.4, end=4.65))    # Db5 - start where you left off
sax.notes.append(pretty_midi.Note(velocity=100, pitch=75, start=4.7, end=5.1))    # Eb5 - reach up, the peak
sax.notes.append(pretty_midi.Note(velocity=75, pitch=70, start=5.2, end=5.95))    # Bb4 - fall, resolve, but not all the way

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
