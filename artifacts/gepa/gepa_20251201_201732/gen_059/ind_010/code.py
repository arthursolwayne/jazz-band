
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (F, C, G, C) with chromatic approaches
bass_notes = []
bar_duration = 1.5
for bar in range(2, 5):  # Bars 2, 3, 4
    time = (bar - 2) * bar_duration
    # Bar 2: F (root), chromatic approach from E
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=time + 0.0, end=time + 0.375))
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=time + 0.375, end=time + 0.75))
    # Bar 3: C (fifth), chromatic approach from B
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time + 0.75, end=time + 1.125))
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=75, start=time + 1.125, end=time + 1.5))
    # Bar 4: G (root), chromatic approach from F#
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=78, start=time + 1.5, end=time + 1.875))
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=77, start=time + 1.875, end=time + 2.25))
    # Bar 4: C (fifth), chromatic approach from B
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=time + 2.25, end=time + 2.625))
    bass_notes.append(pretty_midi.Note(velocity=100, pitch=75, start=time + 2.625, end=time + 3.0))
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # E
]
# Bar 3: C7 (C, E, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # Bb
])
# Bar 4: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
])
piano.notes.extend(piano_notes)

# Sax: Motif on bars 2-4
# Bar 2: Open with a short motif
sax_notes = []
# F7 (F, A, C, Eb) - start with F
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75))
# Play A, resolve on C
sax_notes.append(pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=1.875))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0))
# Bar 3: Play a chromatic line
sax_notes.append(pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.125))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=3.125, end=3.25))
# Bar 4: Return to C, then resolve on G
sax_notes.append(pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.625))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=4.625, end=4.75))
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    time = (bar - 2) * bar_duration
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=time + 0.0, end=time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=time + 1.875, end=time + 2.0)
    # Hihat
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=time + i * 0.1875, end=time + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
