
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
BAR = 1.5

# Key of Eb minor. Dark. Newark at 2am.

# === BAR 1: Little Ray alone (0.0 - 1.5s) ===
# Set it up. Make them wait.
for i in range(8):  # 8 eighth notes
    t = i * BEAT / 2
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=HIHAT, start=t, end=t + 0.1))
    
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0, end=0.2))
drums.notes.append(pretty_midi.Note(velocity=95, pitch=KICK, start=BEAT * 2, end=BEAT * 2 + 0.2))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=BEAT, end=BEAT + 0.15))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=BEAT * 3, end=BEAT * 3 + 0.15))

# === BARS 2-4: Full quartet (1.5 - 6.0s) ===

# Little Ray keeps the pocket
for bar in range(3):
    bar_start = BAR + bar * BAR
    for i in range(8):
        t = bar_start + i * BEAT / 2
        drums.notes.append(pretty_midi.Note(velocity=70, pitch=HIHAT, start=t, end=t + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start, end=bar_start + 0.2))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=KICK, start=bar_start + BEAT * 2, end=bar_start + BEAT * 2 + 0.2))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=bar_start + BEAT, end=bar_start + BEAT + 0.15))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=bar_start + BEAT * 3, end=bar_start + BEAT * 3 + 0.15))

# Marcus - walking line in Eb minor, chromatic approaches, never repeats
# Eb3=51, Db3=49, Cb3=47, Bb2=46, Ab2=44, Gb2=42, E2=40, Eb2=39
marcus_line = [
    (BAR, 51, BEAT * 1.8),           # Eb3 - root, let it breathe
    (BAR + BEAT * 2, 49, BEAT * 0.9),  # Db3
    (BAR + BEAT * 3, 48, BEAT * 0.9),  # C3 chromatic approach
    (BAR * 2, 47, BEAT * 1.8),        # B2 
    (BAR * 2 + BEAT * 2, 46, BEAT * 0.9),  # Bb2
    (BAR * 2 + BEAT * 3, 44, BEAT * 0.9),  # Ab2
    (BAR * 3, 43, BEAT * 1.8),        # G2 - tension
    (BAR * 3 + BEAT * 2, 41, BEAT * 0.9),  # F2
    (BAR * 3 + BEAT * 3, 39, BEAT * 0.9),  # Eb2 - home
]
for start, pitch, dur in marcus_line:
    bass.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=start + dur))

# Diane - 7th chords, comp on 2 and 4, angry but controlled
# Ebm7: Eb-Gb-Bb-Db (51, 54, 58, 61)
# Dbmaj7: Db-F-Ab-C (49, 53, 56, 60)
# Bmaj7#11: B-Eb-Gb-Bb (47, 51, 54, 58) - she's angry
# Ebm9: Eb-Gb-Bb-Db-F (51, 54, 58, 61, 65)

diane_chords = [
    # Bar 2 - Ebm7 on 2 and 4
    (BAR + BEAT, [63, 66, 70, 73], BEAT * 0.7),      # Ebm7 high voicing
    (BAR + BEAT * 3, [61, 66, 70, 73], BEAT * 0.7),  # Dbmaj7/Eb - chromatic inner voice
    # Bar 3 - getting darker
    (BAR * 2 + BEAT, [59, 63, 66, 71], BEAT * 0.7),  # Bmaj7 - the anger
    (BAR * 2 + BEAT * 3, [58, 63, 66, 70], BEAT * 0.7),  # Bbm7
    # Bar 4 - resolve but not too clean
    (BAR * 3 + BEAT, [56, 61, 65, 68], BEAT * 0.7),  # Abm7
    (BAR * 3 + BEAT * 3, [63, 66, 70, 75], BEAT * 0.9),  # Back to Ebm9 - leave it open
]
for start, pitches, dur in diane_chords:
    for p in pitches:
        piano.notes.append(pretty_midi.Note(velocity=65, pitch=p, start=start, end=start + dur))

# Dante - the motif. One question, leave it hanging, come back and answer.
# This is what Wayne's listening for. Make it count.

# The motif: Bb5 to Gb5, down to Eb5, up to F5 - question mark
# Then silence. Let it breathe.
# Come back: Gb5 to Eb5 to Db5 - answer, but leave Db hanging

sax_motif = [
    # Bar 2: The question - starts on the and of 1
    (BAR + BEAT * 0.5, 82, BEAT * 0.8, 95),   # Bb5 - cry out
    (BAR + BEAT * 1.5, 78, BEAT * 0.6, 85),   # Gb5 - drop
    (BAR + BEAT * 2.5, 75, BEAT * 1.2, 90),   # Eb5 - hold it, bend it
    
    # Silence in bar 3 beat 1-2. Let Wayne wonder.
    
    # Bar 3: The answer starts - but hesitant
    (BAR * 2 + BEAT * 2.5, 77, BEAT * 0.5, 80),  # F5 - reach up
    (BAR * 2 + BEAT * 3.25, 78, BEAT * 0.7, 88), # Gb5 - the question again
    
    # Bar 4: Finish it, but don't resolve clean
    (BAR * 3 + BEAT * 0.5, 75, BEAT * 0.9, 92),  # Eb5 - almost home
    (BAR * 3 + BEAT * 2, 73, BEAT * 1.5, 85),    # Db5 - leave it here, unresolved
    # That Db against Diane's Ebm9 - tension that makes you need to hear more
]

for start, pitch, dur, vel in sax_motif:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
