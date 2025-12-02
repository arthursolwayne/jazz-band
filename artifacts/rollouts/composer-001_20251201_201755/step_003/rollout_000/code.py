
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# BAR 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (38) -> F#2 (42) -> A2 (45) -> C#3 (47) -> D2 (38)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=38, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Dmaj7 (D-F#-A-C#), G7 (G-B-D-F), Am7 (A-C-E-G), Dmaj7 (D-F#-A-C#)
# Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=55, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=95, pitch=59, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=95, pitch=66, start=1.5, end=1.75),  # C#

    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5),  # F

    pretty_midi.Note(velocity=95, pitch=69, start=2.875, end=3.125),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=2.875, end=3.125),  # C
    pretty_midi.Note(velocity=95, pitch=74, start=2.875, end=3.125),  # E
    pretty_midi.Note(velocity=95, pitch=77, start=2.875, end=3.125),  # G

    pretty_midi.Note(velocity=95, pitch=55, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=95, pitch=59, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=95, pitch=66, start=3.0, end=3.25),  # C#
]
piano.notes.extend(piano_notes)

# Sax: Motif - D (62) -> F# (66) -> A (69) -> G (67) - leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25)
]
sax.notes.extend(sax_notes)

# BAR 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (38) -> F#2 (42) -> A2 (45) -> C#3 (47) -> D2 (38)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=38, start=4.375, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: G7 (G-B-D-F), Am7 (A-C-E-G), Dmaj7 (D-F#-A-C#), C7 (C-E-G-Bb)
# Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=3.25),  # F

    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=95, pitch=74, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=95, pitch=77, start=3.75, end=4.0),  # G

    pretty_midi.Note(velocity=95, pitch=55, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=95, pitch=59, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=95, pitch=66, start=4.5, end=4.75),  # C#

    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif, resolve on G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5)
]
sax.notes.extend(sax_notes)

# BAR 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (38) -> F#2 (42) -> A2 (45) -> C#3 (47) -> D2 (38)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=38, start=5.875, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Dmaj7 (D-F#-A-C#), Bm7 (B-D-F#-A), G7 (G-B-D-F), Dmaj7 (D-F#-A-C#)
# Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=55, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=95, pitch=59, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=95, pitch=66, start=4.5, end=4.75),  # C#

    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=95, pitch=72, start=5.25, end=5.5),  # A

    pretty_midi.Note(velocity=95, pitch=67, start=5.75, end=6.0),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=5.75, end=6.0),  # B
    pretty_midi.Note(velocity=95, pitch=67, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=95, pitch=70, start=5.75, end=6.0),  # F

    pretty_midi.Note(velocity=95, pitch=55, start=6.0, end=6.25),  # D
    pretty_midi.Note(velocity=95, pitch=59, start=6.0, end=6.25),  # F#
    pretty_midi.Note(velocity=95, pitch=62, start=6.0, end=6.25),  # A
    pretty_midi.Note(velocity=95, pitch=66, start=6.0, end=6.25),  # C#
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif, resolve on G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = 4.5 + (beat * 0.375)
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")
