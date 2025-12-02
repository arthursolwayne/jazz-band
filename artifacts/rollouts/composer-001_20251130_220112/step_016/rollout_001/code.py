
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875)),  # D
    (pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25)), # C
    (pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625)), # Eb
    (pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0)),  # F
    (pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375)),  # E
    (pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75)), # D
    (pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125)), # C
    (pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5)),  # Eb
    (pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875)),  # F
    (pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25)), # E
    (pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625)), # D
    (pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0)),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Drums - Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
    # Add all to drums
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax - Dante: short motif, make it sing
# Motif: D (62), F (65), Ab (68), D (62)
# Bar 2: start on beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=5.625, end=6.0),   # Ab
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
