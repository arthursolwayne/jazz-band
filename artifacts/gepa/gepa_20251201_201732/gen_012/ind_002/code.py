
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2 is 38, F2 is 40) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=39, start=1.5, end=1.875),  # chromatic approach
    pretty_midi.Note(velocity=70, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=70, pitch=43, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=70, pitch=40, start=2.625, end=3.0),  # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on the last bar
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.25),  # E

    # Bar 3: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=75, start=2.25, end=3.0),  # Ab

    # Bar 4: Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.75),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing
# Bar 2: F (65) - Bb (67) - D (69) - rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
]

# Bar 3: F (65) - C (67) - E (69) - rest
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.375),
]

# Bar 4: F (65) - Bb (67) - D (69) - rest
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.625),
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.125),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick_start = bar_start
    snare_start = bar_start + 0.375
    kick_start2 = bar_start + 0.75
    snare_start2 = bar_start + 1.125
    hihat_start = bar_start
    hihat_end = bar_start + 1.5

    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start2, end=kick_start2 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start2, end=snare_start2 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
