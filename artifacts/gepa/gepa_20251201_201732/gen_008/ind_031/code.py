
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
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
hihat_start = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for start in hihat_start:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# Bar 2: Dm7 - D2, F2, A2, C2, chromatic approach on F2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625))  # D2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=1.625, end=1.75))  # F2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=1.875))  # chromatic
bass.notes.append(pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0))  # F2

# Bar 3: G7 - G2, B2, D2, F2, chromatic approach on B2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.125))  # G2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=2.125, end=2.25))  # B2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.375))  # chromatic
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=2.375, end=2.5))  # B2

# Bar 4: Cm7 - C2, Eb2, G2, Bb2, chromatic approach on Eb2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=44, start=2.5, end=2.625))  # C2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=2.75))  # Eb2
bass.notes.append(pretty_midi.Note(velocity=80, pitch=46, start=2.75, end=2.875))  # chromatic
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=2.875, end=3.0))  # Eb2

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 - D, F, A, C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0))  # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0))  # F4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0))  # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0))  # C5

# Bar 3: G7 - G, B, D, F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5))  # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5))  # D5
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5))  # F5

# Bar 4: Cm7 - C, Eb, G, Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0))  # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0))  # Eb4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0))  # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0))  # Bb4 (same as G4)

# Sax: One short motif, make it sing
# Bar 2: Start the motif on D4 (62), then F4 (65), then resolve on Bb4 (67)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick
    kick_start = bar_start + 0.0
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    kick_start = bar_start + 1.125
    kick_end = kick_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare
    snare_start = bar_start + 0.75
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    snare_start = bar_start + 1.875
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    # Hi-hat
    hihat_start = [bar_start + i * 0.375 for i in range(4)]
    for start in hihat_start:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
