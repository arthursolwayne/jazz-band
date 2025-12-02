
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

# Bass line (Marcus): walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=56, start=5.625, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db
# Ab7 = Ab, C, Eb, G
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=68, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=95, pitch=82, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=95, pitch=76, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=95, pitch=80, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=95, pitch=81, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=95, pitch=77, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=95, pitch=87, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=95, pitch=80, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=95, pitch=84, start=3.75, end=4.125), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 -> Bbmaj7 -> Eb7 -> Am7
# Fm7: F, Ab, C, Eb
# Bbmaj7: Bb, D, F, A
# Eb7: Eb, G, Bb, Db
# Am7: A, C, E, G

sax_notes = [
    pretty_midi.Note(velocity=105, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=105, pitch=68, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=105, pitch=72, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=105, pitch=68, start=1.875, end=2.0),  # Eb
    pretty_midi.Note(velocity=105, pitch=71, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=105, pitch=74, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=105, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=105, pitch=69, start=2.375, end=2.5),  # A
    pretty_midi.Note(velocity=105, pitch=68, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=105, pitch=71, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=105, pitch=71, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=105, pitch=76, start=2.875, end=3.0),  # Db
    pretty_midi.Note(velocity=105, pitch=69, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=105, pitch=72, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=105, pitch=76, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=105, pitch=71, start=3.375, end=3.5),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    bar_start = bar * 1.5
    kick_start = bar_start
    kick_end = kick_start + 0.375
    snare_start = bar_start + 0.75
    snare_end = snare_start + 0.375
    hihat_start = bar_start
    hihat_end = bar_start + 1.5

    # Kick
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    # Snare
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    # Hihat
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
