
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
hihat_notes = []
for i in range(0, 8):
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + i * 0.125, end=bar1_start + i * 0.125 + 0.05))
drums.notes.extend(kick_notes + snare_notes + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5
bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar2_start + 0.0, end=bar2_start + 0.25))  # D2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=bar2_start + 0.25, end=bar2_start + 0.5))  # F#2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar2_start + 0.5, end=bar2_start + 0.75))  # A2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar2_start + 0.75, end=bar2_start + 1.0))  # A2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar3_start + 0.0, end=bar3_start + 0.25))  # D2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=bar3_start + 0.25, end=bar3_start + 0.5))  # F#2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar3_start + 0.5, end=bar3_start + 0.75))  # A2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar3_start + 0.75, end=bar3_start + 1.0))  # A2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar4_start + 0.0, end=bar4_start + 0.25))  # D2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=41, start=bar4_start + 0.25, end=bar4_start + 0.5))  # F#2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar4_start + 0.5, end=bar4_start + 0.75))  # A2
bass_notes.append(pretty_midi.Note(velocity=90, pitch=43, start=bar4_start + 0.75, end=bar4_start + 1.0))  # A2
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = []
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 0.0, end=bar2_start + 1.0))  # D4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.0, end=bar2_start + 1.0))  # F#4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 0.0, end=bar2_start + 1.0))  # A4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=74, start=bar2_start + 0.0, end=bar2_start + 1.0))  # C#5
# Bar 3: G7 (G-B-D-F)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar3_start + 0.0, end=bar3_start + 1.0))  # G4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + 0.0, end=bar3_start + 1.0))  # B4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar3_start + 0.0, end=bar3_start + 1.0))  # D4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar3_start + 0.0, end=bar3_start + 1.0))  # F4
# Bar 4: A7 (A-C#-E-G)
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 0.0, end=bar4_start + 1.0))  # A4
piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar4_start + 0.0, end=bar4_start + 1.0))  # C#5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar4_start + 0.0, end=bar4_start + 1.0))  # E5
piano_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 0.0, end=bar4_start + 1.0))  # G4
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
bar2_notes = []
bar3_notes = []
bar4_notes = []
for i in range(0, 8):
    bar2_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + i * 0.125, end=bar2_start + i * 0.125 + 0.05))
    bar3_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + i * 0.125, end=bar3_start + i * 0.125 + 0.05))
    bar4_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + i * 0.125, end=bar4_start + i * 0.125 + 0.05))
drums.notes.extend(bar2_notes + bar3_notes + bar4_notes)

# Sax: One short motif, start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 - D4 (start on 2, end on 4)
sax_notes = []
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 0.0, end=bar2_start + 0.1))  # D4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.1, end=bar2_start + 0.2))  # F#4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 0.2, end=bar2_start + 0.3))  # A4
sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar4_start + 0.5, end=bar4_start + 0.6))  # D4
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
