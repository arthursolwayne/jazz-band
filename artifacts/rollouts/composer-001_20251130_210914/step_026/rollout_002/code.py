
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

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0), # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5), # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75), # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=3.0), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.5), # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=52, start=3.5, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.0), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.25), # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.25, end=4.5), # C
    # Bar 4 continuation
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0), # G
    pretty_midi.Note(velocity=90, pitch=51, start=5.0, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.5), # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.5, end=5.75), # C
    pretty_midi.Note(velocity=90, pitch=50, start=5.75, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    # Dm7: D, F, A, C
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.75), # A
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.75), # C
    # Bar 3
    # G7: G, B, D, F
    pretty_midi.Note(velocity=95, pitch=71, start=2.5, end=2.75), # G
    pretty_midi.Note(velocity=95, pitch=73, start=2.5, end=2.75), # B
    pretty_midi.Note(velocity=95, pitch=76, start=2.5, end=2.75), # D
    pretty_midi.Note(velocity=95, pitch=77, start=2.5, end=2.75), # F
    # Bar 4
    # Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=95, pitch=60, start=3.5, end=3.75), # C
    pretty_midi.Note(velocity=95, pitch=62, start=3.5, end=3.75), # Eb
    pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75), # G
    pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75), # Bb
]
piano.notes.extend(piano_notes)

# You: Motif in Dm
# Start with D (62), Bb (67), F (64), C (69)
# Leave it hanging on the 4th beat
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0), # C
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625), # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875), # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0), # C
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625), # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.875), # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.0), # C
    # Return to motif
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0), # C
    # End with D
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75), # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start
    kick_end = kick_start + 0.375
    kick_3_start = kick_start + 1.125
    kick_3_end = kick_3_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_3_start, end=kick_3_end))
    # Snare on 2 and 4
    snare_start = start + 0.75
    snare_end = snare_start + 0.125
    snare_4_start = start + 1.875
    snare_4_end = snare_4_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_4_start, end=snare_4_end))
    # Hihat on every eighth
    for i in range(0, 8):
        hihat_start = start + (i * 0.1875)
        hihat_end = hihat_start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
