
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line, chromatic approaches, never the same note twice. Dm7 -> G7 -> Cmaj7 -> F7
# Dm7: D F A C
# G7: G Bb D F
# Cmaj7: C E G B
# F7: F A C Eb

# Bar 2 (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # C
]

# Bar 3 (3.0 - 4.5s)
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # F
]

# Bar 4 (4.5 - 6.0s)
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords, comp on 2 and 4 (Dm7, G7, Cmaj7, F7)
# Bar 2: Dm7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # C
]

# Bar 3: G7 on beat 2
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # F
]

# Bar 4: Cmaj7 on beat 2
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # B
]

# Bar 4: F7 on beat 4
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F# (66) -> C (60) -> D (62) -> leave it hanging on F# (66) at bar 2
# Come back and finish with C (60) and D (62)

# Bar 2: D -> F# -> C -> D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D
]

# Leaving it hanging on F# at bar 2
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),
]

# Coming back and finishing with C and D in bar 4
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)

    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
