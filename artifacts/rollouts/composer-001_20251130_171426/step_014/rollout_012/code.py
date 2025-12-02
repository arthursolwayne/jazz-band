
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.0, end=bar1_start + 0.1),
              pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 0.85)]
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.475),
               pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.225)]
hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.0, end=bar1_start + 0.05),
               pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.1875, end=bar1_start + 0.2375),
               pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.425),
               pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.5625, end=bar1_start + 0.6125),
               pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.75, end=bar1_start + 0.8),
               pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 0.9375, end=bar1_start + 0.9875),
               pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.175),
               pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + 1.3125, end=bar1_start + 1.3625)]
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drum pattern for bars 2-4
bar2_start = 1.5
bar2_end = 3.0
bar3_start = 3.0
bar3_end = 4.5
bar4_start = 4.5
bar4_end = 6.0

def add_drums(start):
    kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.1),
                  pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.85)]
    snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.475),
                   pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.225)]
    hihat_notes = [pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.05),
                   pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.2375),
                   pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.425),
                   pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.6125),
                   pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.8),
                   pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 0.9875),
                   pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.175),
                   pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.3625)]
    drums.notes.extend(kick_notes + snare_notes + hihat_notes)

add_drums(bar2_start)
add_drums(bar3_start)
add_drums(bar4_start)

# Bass line (Marcus): Walking line, chromatic approaches
# Fm7 = F, Ab, C, Eb
# Walking line in Fm: F, Gb, G, Ab, A, Bb, B, C, Db, D, Eb, E, F
# Bars 2-4
bass_notes = []
for bar in [bar2_start, bar3_start, bar4_start]:
    # Bar 1: F -> Gb -> G -> Ab
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=bar + 0.0, end=bar + 0.15))  # F
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar + 0.15, end=bar + 0.3))  # Gb
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=66, start=bar + 0.3, end=bar + 0.45))  # G
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar + 0.45, end=bar + 0.6))  # Ab
    # Bar 2: A -> Bb -> B -> C
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar + 0.6, end=bar + 0.75))  # A
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=68, start=bar + 0.75, end=bar + 0.9))  # Bb
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar + 0.9, end=bar + 1.05))  # B
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar + 1.05, end=bar + 1.2))  # C
    # Bar 3: Db -> D -> Eb -> E
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=61, start=bar + 1.2, end=bar + 1.35))  # Db
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar + 1.35, end=bar + 1.5))  # D
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar + 1.5, end=bar + 1.65))  # Eb
    bass_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=bar + 1.65, end=bar + 1.8))  # E
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bars 2-4
piano_notes = []
for bar in [bar2_start, bar3_start, bar4_start]:
    # Bar 1: Fm7 on 2 and 4
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=bar + 0.375, end=bar + 0.5))  # F
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar + 0.375, end=bar + 0.5))  # Ab
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar + 0.375, end=bar + 0.5))  # C
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar + 0.375, end=bar + 0.5))  # Eb
    # Bar 2: Fm7 on 2 and 4
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=bar + 1.125, end=bar + 1.25))  # F
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar + 1.125, end=bar + 1.25))  # Ab
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar + 1.125, end=bar + 1.25))  # C
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar + 1.125, end=bar + 1.25))  # Eb
piano.notes.extend(piano_notes)

# Sax solo (Dante): Short motif, make it sing
# Fm scale: F, Gb, G, Ab, A, Bb, B, C, Db, D, Eb, E
# Motif: F - Gb - G - Ab (hanging on Ab)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.0, end=bar2_start + 0.15),
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 0.15, end=bar2_start + 0.3),
    pretty_midi.Note(velocity=100, pitch=66, start=bar2_start + 0.3, end=bar2_start + 0.45),
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 0.45, end=bar2_start + 0.6),
    # Return on bar 4, ending on Eb (64) to resolve
    pretty_midi.Note(velocity=100, pitch=64, start=bar4_start + 1.35, end=bar4_start + 1.5)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
