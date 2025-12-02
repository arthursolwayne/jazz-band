
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: F (38) -> G (43), chromatic approach from E (41)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.625)) # chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.625, end=1.875)) # F (root)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.125)) # G (fifth)

# Bar 3: Bb (46) -> C (48), chromatic approach from A (45)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=2.625)) # chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=46, start=2.625, end=2.875)) # Bb (root)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=48, start=2.875, end=3.125)) # C (fifth)

# Bar 4: D (43) -> E (47), chromatic approach from D# (44)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=44, start=3.5, end=3.625)) # chromatic approach
bass.notes.append(pretty_midi.Note(velocity=100, pitch=43, start=3.625, end=3.875)) # D (root)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=3.875, end=4.125)) # E (fifth)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)) # F (F4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0)) # A (A4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0)) # C (C5)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0)) # E (E5)

# Bar 3: Bb7 (Bb, D, F, A)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=3.0)) # Bb (Bb4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0)) # D (D4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0)) # F (F4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0)) # A (A4)

# Bar 4: D7 (D, F#, A, C)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0)) # D (D4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0)) # F# (F#4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0)) # A (A4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0)) # C (C5)

# Sax: Dante, one short motif, start it, leave it hanging, come back and finish it
# Motif: F, Ab, Bb, resolve on F in bar 4

# Bar 2: Start motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625)) # F (F4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=1.625, end=1.75)) # Ab (Ab4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=1.875)) # Bb (Bb4)

# Bar 4: Resolve on F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625)) # F (F4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=3.75)) # F (F4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=3.875)) # F (F4)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3 for each bar
for bar in range(0, 3):
    start = 1.5 + bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    kick_start = start + 0.75
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))

# Snare on 2 and 4 for each bar
for bar in range(0, 3):
    start = 1.5 + bar * 1.5
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    snare_start = start + 1.875
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))

# Hi-hat on every eighth
for i in range(0, 6):
    start = 1.5 + i * 0.375
    end = start + 0.125
    if end <= 6.0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_moment.mid")
