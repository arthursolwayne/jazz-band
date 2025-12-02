
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38) -> G (43) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    # Bar 3: C (40) -> D (45) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=45, start=3.25, end=3.625),
    # Bar 4: G (43) -> A (47) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=3.625, end=3.875),
    pretty_midi.Note(velocity=90, pitch=45, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=47, start=4.25, end=4.625),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # Eb
]
# Bar 3: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.875), # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.875), # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=2.875), # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.875), # Bb
])
# Bar 4: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=78, start=3.625, end=3.875), # G
    pretty_midi.Note(velocity=100, pitch=81, start=3.625, end=3.875), # B
    pretty_midi.Note(velocity=100, pitch=83, start=3.625, end=3.875), # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.625, end=3.875), # F
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (69), Ab (71), Bb (72), F (69) — short and angular
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=71, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
