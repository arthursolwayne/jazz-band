
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches
bass_notes = [
    # Bar 2: D F# A C
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=70, pitch=64, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=70, pitch=69, start=2.625, end=3.0),  # C
    # Bar 3: D B C# D
    pretty_midi.Note(velocity=70, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=70, pitch=69, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=70, pitch=71, start=3.75, end=4.125), # C#
    pretty_midi.Note(velocity=70, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4: D F# A C
    pretty_midi.Note(velocity=70, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=70, pitch=64, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=70, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=70, pitch=69, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # F#
    # Bar 3: D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875), # F#
]
piano.notes.extend(piano_notes)

# Sax: Melody
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F#
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # A
    # Bar 4: Finish it
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
for bar in range(2, 4):
    bar_start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    kick_start = bar_start + 0.0
    kick_end = kick_start + 0.375
    kick_start_3 = bar_start + 1.125
    kick_end_3 = kick_start_3 + 0.375
    # Snare on 2 and 4
    snare_start = bar_start + 0.75
    snare_end = snare_start + 0.125
    snare_start_4 = bar_start + 1.875
    snare_end_4 = snare_start_4 + 0.125
    # Hihat on every eighth
    for i in range(8):
        hihat_start = bar_start + i * 0.1875
        hihat_end = hihat_start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))
    # Add kick
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start_3, end=kick_end_3))
    # Add snare
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start_4, end=snare_end_4))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
